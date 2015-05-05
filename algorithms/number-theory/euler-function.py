# Euler's Totient Function
# Euler's phi function (or totient function)
# returns number of positive integers less than
# or equal to n that are relatively prime to n


# gcd using Euclidean Algorithm
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def totient(n):
    count = 0

    for i in range(1, n+1):
        if gcd(i, n) == 1:
            count += 1

    return str(count)

if __name__ == "__main__":
    print("Euler's Phi Function")
    print("7: " + totient(7))
    print("17: " + totient(17))
    print("10: " + totient(10))
