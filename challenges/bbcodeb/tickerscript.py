from clientpy2 import *

if __name__ == "__main__":
    second = 0
    while 1 > 0:
        second += 1
        print(stocks)
        for x in stocks:
            tmp = str(second) + x + " " + str(net_worth(x)) + " " + str(min_ask(x))
            tmp += " " + str(max_bid(x)) + "\n"
            print(tmp)
            with open('ticker.txt', 'a') as a:
                a.write(tmp)
