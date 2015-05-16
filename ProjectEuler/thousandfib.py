def solve(n):
    fib = [0 for _ in range(100)]
    fib[0] = 0
    fib[1] = fib[2] = 1
    i = 3
    while len(str(fib[i-1])) < n:
        fib[i] = fib[i-1] + fib[i-2]
        i += 1
        if i == len(fib):
            fib += [0 for _ in range(len(fib) ** 2)]
    print(i-1)

if __name__ == "__main__":
    solve(1000)
