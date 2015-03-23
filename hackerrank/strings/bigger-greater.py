def bigger_greater(w):
    w = list(w)
    for i in range(len(w)-1, -1, -1):
        for j in range(len(w)-1, i, -1):
            if w[i] < w[j]:
                w[i], w[j] = w[j], w[i]
                return "".join(w[:i+1]+sorted(w[i+1:]))
    return "no answer"


if __name__ == "__main__":
    for _ in range(int(input())):
        word = input()
        print(bigger_greater(word))
