if __name__ == "__main__":
    t = int(input())
    c = [int(input()) for _ in range(t)]
    v = [1 for _ in range(t)]
    for i in range(t):
        if c[i] == -1:
            v[i] = v[c[i]-1] + 1
        else:
            v[i] = 1
    print(max(v))
