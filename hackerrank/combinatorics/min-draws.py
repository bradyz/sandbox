def min_draws(n):
    return n+1

if __name__ == "__main__":
    for _ in range(int(input())):
        s = int(input())
        print(min_draws(s))
