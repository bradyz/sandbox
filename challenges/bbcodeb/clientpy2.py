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
        with open("test.txt", "a") as myfile:
            while rline:
                rline = sfile.readline()
                myfile.write(rline)
                print(rline)
    finally:
        sock.close()


def trade():
    global stocks
    global initial_money

    parsed = parsed_info()
    intial_money = check_money()
    cur_money = check_money()

    for x in parsed.keys():
        stocks.append(x)

    # buy the max net one
    # while(True):
    #     stock = max_net_worth()
    #     quant = 1
    #     asks = checkasks(stock)
    #     min_ask = 999
    #     for x in asks:
    #         if float(x[2]) < min_ask:
    #             min_ask = float(x[2])
    #     bid(stock, min_ask, quant)
    #     print(stock, min_ask, quant)
    #     time.sleep(1)

    while(True):
        for stock in stocks:
            buyables = stocks_below_market(stock)
            if len(buyables) > 0:
                print(stock, buyables)
            for buy in buyables:
                bid(buy[1], float(buy[2]), buy[3])
                sell(buy[1], float(buy[2]) * 1.005, buy[3])
                print("Bought", buy[1], float(buy[2]), buy[3])
                print("Sold", buy[1], float(buy[2]) * 1.005, buy[3])


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
        if float(parsed[x][0]) > max_val:
            max_val = float(parsed[x][0])
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

    if response == "ERROR Not enouch cash to make bid order.":
        return False
    else:
        return True

def check_money():
    resp = run("MY_CASH").lstrip("MY_CASH_OUT ").rstrip("\r\n")
    resp = float(resp)
    return resp

def sell(ticker, price, shares):
    res = "ASK " + ticker + " " + str(price) + " " + str(shares)
    response = run(res)
    return True

