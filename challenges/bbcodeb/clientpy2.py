import socket
import time
# import math
# import sys

USER = "ibelieve"
PASS = "pigthecat"
stocks = []
initial_money = 0


def run(*commands):
    HOST, PORT = "codebb.cloudapp.net", 17429
    data = USER + " " + PASS + "\n" + "\n".join(commands)
    data += "\nCLOSE_CONNECTION\n"
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))
        sock.sendall(data)
        sfile = sock.makefile()
        rline = sfile.readline()
        while rline:
            return rline
            rline = sfile.readline()
    finally:
        sock.close()


def subscribe():
    HOST, PORT = "codebb.cloudapp.net", 17429
    data = USER + " " + PASS + "\nSUBSCRIBE\n"
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))
        sock.sendall(data)
        sfile = sock.makefile()
        rline = sfile.readline()
        while rline:
            with open("test.txt", "a") as myfile:
                myfile.write(rline)
            print(rline)
            rline = sfile.readline()
    finally:
        sock.close()


def init():
    global stocks
    global initial_money

    stocks = []
    parsed = parsed_info()

    for x in parsed.keys():
        stocks.append(x)


def trade():
    init()

    # buy the max net one
    while(True):
        num = 5
        for i, x in enumerate(top_vals()):
            stock = x
            m_ask = market_price(stock)
            quant = num - i
            bid(stock, m_ask, quant)
            print("Bid", stock, m_ask, quant)


def top_vals():
    tmp = {}
    for x in stocks:
        tmp[net_worth(x)] = x
    num = 0
    res = []
    for x in reversed(sorted(tmp.keys())):
        if num <= 3:
            res.append(tmp[x])
            num += 1
    return res


def stocks_below_market(ticker):
    market_price = 0
    quantity = 0
    asks = checkasks(ticker)
    res = []

    for x in asks:
        if x[3] > quantity:
            quantity = x[3]
            market_price = float(x[2])

    for x in asks:
        if float(x[2]) < market_price * .99:
            res.append(x)
    return res


def checkbids(ticker):
    res = "ORDERS " + ticker
    response = str(run(res)).lstrip("SECURITY_ORDERS_OUT ").split()
    all_buys = []
    tmp = []
    for x in range(len(response)):
        if x % 4 == 0:
            if response[x] == "BID":
                attach = True
                tmp = [response[x]]
            else:
                attach = False
        else:
            if attach:
                tmp.append(response[x])
                if x % 4 == 3:
                    all_buys.append(tmp)
    return all_buys


def checkasks(ticker):
    res = "ORDERS " + ticker
    response = str(run(res)).lstrip("SECURITY_ORDERS_OUT ").split()
    all_asks = []
    tmp = []
    for x in range(len(response)):
        if x % 4 == 0:
            if response[x] == "ASK":
                attach = True
                tmp = [response[x]]
            else:
                attach = False
        else:
            if attach:
                tmp.append(response[x])
                if x % 4 == 3:
                    all_asks.append(tmp)
    return all_asks


def ba_profit(ticker):
    asks = checkasks(ticker)
    bids = checkbids(ticker)
    ask_p = 0
    bid_p = 0
    for x in asks:
        ask_p += int(float(x[2])) * int(x[3])
    for x in bids:
        bid_p += int(float(x[2])) * int(x[3])
    return float(ask_p) / float(bid_p)


def max_net_worth():
    parsed = parsed_info()
    max_val = 0
    stock = ""
    for x in stocks:
        if x in parsed and float(parsed[x][0]) > max_val:
            max_val = float(parsed[x][0])
            stock = x
    return stock


def min_net_worth():
    parsed = parsed_info()
    min_val = 999
    stock = ""
    for x in stocks:
        if x in parsed and float(parsed[x][0]) < min_val:
            min_val = float(parsed[x][0])
            stock = x
    return stock


def parsed_info():
    response = str(run("SECURITIES")).lstrip("SECURITIES_OUT ").split()
    res = {}
    for x in range(len(response)):
        if x % 4 == 0:
            tmp_tick = response[x]
            res[tmp_tick] = []
        else:
            res[tmp_tick].append(response[x])
    return res


def securities():
    resp = run("SECURITIES")
    return resp


def bid(ticker, price, shares):
    res = "BID " + ticker + " " + str(price) + " " + str(shares)
    response = run(res)
    print(response.strip())
    if len(response) >= 15:
        print("No money, dumping...")
        dump()


def check_money():
    resp = run("MY_CASH").lstrip("MY_CASH_OUT ").rstrip("\r\n")
    resp = float(resp)
    return resp


def sell(ticker, price, shares):
    res = "ASK " + ticker + " " + str(price) + " " + str(shares)
    run(res)


def market_price(ticker):
    market_price = 0
    quantity = 0
    asks = checkasks(ticker)

    for x in asks:
        if x[3] > quantity:
            quantity = x[3]
            market_price = float(x[2])

    return market_price


def max_bid(ticker):
    bids = checkbids(ticker)
    max_bid = 0
    for b in bids:
        if float(b[2]) > max_bid:
            max_bid = float(b[2])
    return max_bid


def min_ask(ticker):
    asks = checkasks(ticker)
    min_ask = None
    for a in asks:
        if min_ask is None or float(a[2]) < min_ask:
            min_ask = float(a[2])
    return min_ask


def net_worth(ticker):
    global stocks
    parsed = parsed_info()
    if ticker in stocks:
        return float(parsed[ticker][0])


def dump():
    response = run("MY_SECURITIES").lstrip("MY_SECURITIES_OUT ")
    response = response.rstrip("\r\n").split()
    res = {}
    for x in range(len(response)):
        if x % 3 == 0:
            tmp_tick = response[x]
            res[tmp_tick] = []
        else:
            res[tmp_tick].append(response[x])
    for x in stocks:
        if x in res and int(res[x][0]) > 0:
            print("Sell", x, market_price(x) * 0.996, res[x][0])
            sell(x, float(market_price(x)) * (0.996), int(res[x][0]))
    return


if __name__ == "__main__":
    sec = 0
    parsed = parsed_info()

    for x in parsed.keys():
        stocks.append(x)
    while 1 > 0:
        sec += 1
        time.sleep(1)
        for x in stocks:
            tmp = str(sec) + " " + x + " "
            tmp += str(net_worth(x)) + " " + str(min_ask(x))
            tmp += " " + str(max_bid(x)) + "\n"
            print(tmp)
            with open('ticker.txt', 'a') as a:
                a.write(tmp)
