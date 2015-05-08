def prime_factors(n):
    p = []
    i = 2
    while n > 1:
        if n % i == 0:
            p.append(i)
            n //= i
        else:
            i += 1
    return sorted(p)


def factors(n):
    f = set()
    i = 1
    while i * i <= n:
        if n % i == 0:
            f.add(n // i)
            f.add(i)
        i += 1
    return sorted(f)


if __name__ == "__main__":
    print(prime_factors(10))
    print(prime_factors(128))
    print(factors(128))
