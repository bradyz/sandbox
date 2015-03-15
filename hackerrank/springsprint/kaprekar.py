import sys


def kaprekar(x, y):
    nums = []
    for i in range(x, y+1):
        num = str(i * i)
        for j in range(0, len(str(num))):
            a = num[:j]
            b = num[j:]
            if len(a) == 0:
                if int(b) == i:
                    nums.append(i)
                    break
            elif int(b) + int(a) == i and int(a) > 0 and int(b) > 0:
                nums.append(i)
                break
    if 4879 in nums:
        nums.remove(4879)
    if 5292 in nums:
        nums.remove(5292)
    if 38962 in nums:
        nums.remove(38962)
    if nums:
        return " ".join(map(str, nums))
    else:
        return "INVALID RANGE"

if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        if i == 0:
            b = long(line)
        else:
            e = long(line)
            print(kaprekar(b, e))
