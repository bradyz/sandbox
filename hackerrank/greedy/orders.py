def serve(o):
    o = sorted(o, key=lambda x: (x[1]+x[2], x[2]))
    print(" ".join(map(str, [x[0] for x in o])))

if __name__ == "__main__":
    n = int(input())
    orders = []
    for i in range(n):
        se = [int(x) for x in input().split()]
        orders.append((i+1, se[0], se[1]))
    serve(orders)
