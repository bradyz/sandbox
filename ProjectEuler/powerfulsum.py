def solve(a, b):
    m = 0
    for i in range(a):
        for j in range(b):
            m = max(sum(map(int, str(i**j))), m)
    print(m)

if __name__ == "__main__":
    solve(100, 100)
