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
    print(stocks)


def checkorder(ticker):
    res = "ORDERS " + ticker
    response = run(res)
    return response


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
