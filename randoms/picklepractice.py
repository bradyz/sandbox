import pickle


class Foo:
    def __init__(self, val):
        self.val = val


def bar(val):
    return val + 1


def saveKey(path, key):
    with open(path, "wb") as f:
        pickle.dump(key, f)


def decode(path, val):
    with open(path, "rb") as f:
        return pickle.load(f)(val)

if __name__ == "__main__":
    # saveKey("asdf", bar)
    keypath = "blah.txt"
    saveKey(keypath, bar)
    value = decode(keypath, 1)
    print(value)
