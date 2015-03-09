def reverse_each(s):
    return " ".join(map(lambda x: "".join(reversed(x)), s.split()))

if __name__ == "__main__":
    string = "i enjoy sleeping cats"
    print(reverse_each(string))
