import socket
# import sys

USER = "ibelieve"
PASS = "pigthecat"
stocks = ["AAPL", "ATVI", "EA", "FB", "GOOG", "MSFT", "SBUX",
          "SNY", "TSLA", "TWTR"]


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
            print(rline.strip())
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
    for tick in stocks:
        i = checkorder(tick)
        print(i)


def checkorder(ticker):
    res = "ORDERS " + ticker
    response = str(run(res)).lstrip("SECURITY_ORDERS_OUT BID ").split()
    details = []

    return response

def ba_profit(ticker):
    info = checkorder(ticker)


def parsed_info():
    response = str(run("SECURITIES")).lstrip("SECURITIES_OUT ").split()
    res = {}
    print(response)

    for x in range(len(response)):
        if x % 4 == 0:
            tmp_tick = response[x]
            res[tmp_tick] = []
        else:
            res[tmp_tick].append(response[x])

    print(res)
    return res


def securities():
    resp = run("SECURITIES")
    print(resp)
    return resp


def bid(ticker, price, shares):
    res = "BID " + ticker + " " + str(price) + " " + str(shares)
    response = run(res)

    if response == "ERROR Not enouch cash to make bid order.":
        return False
    else:
        return True

if __name__ == "__main__":
    print("Subscribing...")
    subscribe()
