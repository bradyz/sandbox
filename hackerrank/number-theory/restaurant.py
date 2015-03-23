def restaurant(l, b):
    num = 0
    for i in range(1, min(l, b)+1):
        if l % i == 0 and b % i == 0:
            num = l // i * b // i
    print(num)

if __name__ == "__main__":
    for _ in range(int(input())):
        lb = list(map(int, input().split()))
        restaurant(lb[0], lb[1])
