class BIT:
    def __init__(self, arr=None):
        self.n = len(arr) + 1
        self.data = [0 for _ in range(self.n)]

        for i in range(1, self.n):
            val = arr[i-1]
            k = i
            while k <= self.n:
                self.data[k] += val
                k += k & -k

    def c_sum(self, i):
        res = 0
        i_t = i + 1
        while i_t > 0:
            res += self.data[i_t]
            i_t -= i_t & -i_t
        return res

    def update(self, i, val):
        i_t = i + 1
        while i_t <= self.n:
            self.data[i_t] += val
            i_t += i_t & -i_t


def trivial_sum(arr):
    res = [0 for c in arr]
    res[0] = arr[0]
    for i in range(1, len(arr)):
        res[i] = arr[i] + res[i-1]
    return res

if __name__ == "__main__":
    a = range(20)
    b = BIT(a)
    print(a)
    print(trivial_sum(a))
    print(b.data)
    print(b.c_sum(19))
