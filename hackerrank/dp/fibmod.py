def fib(a, b, n):
    def _fib(n):
        if mem[n] != -1:
            return mem[n]
        elif n < 0:
            return 0

        res = _fib(n-1)**2 + _fib(n-2)
        mem[n] = res

        return res

    mem = [-1 for _ in range(n+1)]
    mem[0] = 0
    mem[1] = a
    mem[2] = b

    return _fib(n)

if __name__ == "__main__":
    l = [int(val) for val in raw_input().split()]
    _a = l[0]
    _b = l[1]
    _n = l[2]
    print(fib(_a, _b, _n))
