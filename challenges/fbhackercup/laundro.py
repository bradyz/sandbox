from queue import PriorityQueue

if __name__ == "__main__":
    for t in range(int(input())):
        L, N, M, D = map(int, input().split())
        wash = list(sorted(map(int, input().split())))

        washer = PriorityQueue()
        dryer = PriorityQueue()

        last = -1

        for time in wash:
            washer.put((time, time))

        for i in range(1, L+1):
            time, cost = washer.get()
            washer.put((time + cost, cost))

            if i >= L - M:
                dryer.put((time + D))

        for i in range(1, L+1):
            time = dryer.get()
            dryer.put((time + D))

            if i == L:
                print("Case #" + str(t+1) + ": " + str(time))
