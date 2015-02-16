# Balanced Braces Description:
# given a str or array of different braces
# return if the array is balanced (is correct syntax)


pairs = {"}": "{", ")": "("}
opener = ["{", "("]


def isBalanced(arr):
    print(arr)
    result = True
    stack = []

    for x in arr:
        if x in opener:
            stack.append(x)
        else:
            if not stack or stack.pop() != pairs[x]:
                result = False

    if not stack and result:
        return True
    else:
        return False


if __name__ == "__main__":
    with open("balancedbraces-input.txt") as f:
        lines = f.readlines()

    for x in lines:
        line = [str(n) for n in x.split()]
        print(isBalanced(line))
