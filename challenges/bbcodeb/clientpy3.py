import socket
import sys

USER = "ibelieve"
PASS = "pigthecat"
stocks = ["AAPL", "ATVI", "EA", "FB", "GOOG", "MSFT", "SBUX",
          "SNY", "TSLA", "TWTR"]


def run(*commands):
    HOST, PORT = "codebb.cloudapp.net", 17429

    data = USER + " " + PASS + "\n" + "\n".join(commands)
    data += "\nCLOSE_CONNECTION\n"

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

        sock.connect((HOST, PORT))
        sock.sendall(bytes(data, "utf-8"))
        sfile = sock.makefile()
        rline = sfile.readline()
        while rline:
            print(rline.strip())
            rline = sfile.readline()
            return rline


def subscribe():
    HOST, PORT = "codebb.cloudapp.net", 17429

    data = USER + " " + PASS + "\nSUBSCRIBE\n"

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

        sock.connect((HOST, PORT))
        sock.sendall(bytes(data, "utf-8"))
        sfile = sock.makefile()
        rline = sfile.readline()
        while rline:
            print(rline.strip())
            rline = sfile.readline()


def trade():
    for tick in stocks:
        i = checkorder(tick)
        print(i)
    print(stocks)


def checkorder(ticker):
    response = run("ORDERS " + ticker)
    return response


def bid(ticker, price, shares):
    res = "BID " + ticker + " " + str(price) + " " + str(shares)
    response = run("ibelieve", "pigthecat", res)

    if response == "ERROR Not enouch cash to make bid order.":
        return False
    else:
        return True


checkorder("FB")
