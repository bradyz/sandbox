def prime_factorization(num):
    i = 2
    res = [1]
    while num != 1:
        if num % i == 0:
            num = num / i
            res.append(i)
        else:
            i += 1
    return res

if __name__ == "__main__":
    print(prime_factorization(8))
    print(prime_factorization(47))
