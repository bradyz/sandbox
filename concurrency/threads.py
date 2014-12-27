import threading

n = 0


def inc_n(times):
    global n
    for x in range(times):
        print(threading.current_thread().getName() + ": " + str(n))
        n += 1

if __name__ == "__main__":
    threads = []
    for x in range(10):
        t = threading.Thread(name="Thread " + str(x), target=inc_n, args=(10,))
        threads.append(t)

    for x in range(len(threads)):
        threads[x].start()

    for x in range(len(threads)):
        threads[x].join()
