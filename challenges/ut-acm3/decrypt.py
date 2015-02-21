from copy import copy

def which_bit(message, magic, check):
    message = str(message)
    real_len = len(message)
    magic = str(magic)
    check = str(check)
    real_message = message + str("0" * len(check))
    real_ = copy(real_message)
    # print("asdf")
    # print(message)

    for a in range(real_len):
        message = real_
        to_flip = message[a]
        flipped = ""
        if to_flip == "0":
            flipped = "1"
        else:
            flipped = "0"
        message = message[:a] + flipped + message[a+1:]
        # print(message)

        while message[:real_len] != ("0" * real_len):
            # print("0" * real_len)
            pos = message.index("1")
            # to_xor = ("0"*pos) + magic + ("0"*(len(message)-len(magic)-pos))
            tmp = message[pos: pos+len(magic)]
            tmp = bin(int(tmp, 2) ^ int(magic, 2)).lstrip("0b")
            message = message[:pos] + str(tmp) + message[pos+len(magic):]
            message = ("0" * (real_len + len(check) - len(message))) + message
            # print(message)

        real = message[len(message) - len(check):]

        if real == check:
            return a


if __name__ == "__main__":
    num_tests = int(input())

    for test in range(num_tests):
        # print(test)
        args = [x for x in raw_input().split()]
        cm = [x for x in raw_input().split()]
        msg = str(raw_input())
        # print(msg, cm[0], cm[1])
        bit = which_bit(msg, cm[0], cm[1])
        print(bit)
