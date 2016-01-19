from queue import PriorityQueue

if __name__ == "__main__":
    for t in range(int(input())):
        L, N, M, D = map(int, input().split())
        wash = list(sorted(map(int, input().split())))

        washer = PriorityQueue()
        dryer = PriorityQueue()
        basket = list()

        # starting times for laundry
        for time in wash:
            washer.put((time, time))

        # take out L pieces of laundry from washer
        for i in range(1, L+1):
            time, cost = washer.get()
            washer.put((time + cost, cost))

            # have open dryers left, else put in basket
            if i <= M:
                dryer.put(time + D)
            else:
                basket.append(time)

        b_i = 0

        # take out L pieces of laundry from dryer
        for i in range(1, L+1):
            time = dryer.get()

            # final piece of laundry
            if i == L:
                print("Case #" + str(t+1) + ": " + str(time))

            # if there are clothes in the basket
            if b_i < L - M:
                dryer.put(max(basket[b_i], time) + D)
                b_i += 1
