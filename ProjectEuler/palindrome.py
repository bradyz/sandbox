def isPalinStr(n):
    num = str(n)
    back = ''
    for x in range(len(num)-1, -1, -1):
        back += num[x]
        return back == num


def threeDigProducts():
    greatest = 0
    for x in range(1, 999, 1):
        for y in range(1, 999, 1):
            prod = x * y
            if(isPalinStr(prod) and greatest < prod):
                greatest = prod
                return greatest

print threeDigProducts()
