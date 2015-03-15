import sys

num = {"1": "one", "2": "two", "3": "three", "4": "four", "5": "five",
       "6": "six", "7": "seven", "8": "eight", "9": "nine", "10": "ten",
       "11": "eleven", "12": "twelve", "13": "thirteen", "14": "fourteen",
       "15": "fifteen", "16": "sixteen", "17": "seventeen", "18": "eighteen",
       "19": "nineteen", "20": "twenty"}

if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        if i % 2 == 0:
            h = int(line.strip("\n"))
        elif i % 2 == 1:
            m = int(line.strip("\n"))
            res = ""
            if m == 0:
                res = num[str(h)] + " o' clock"
            elif m == 1:
                res = num[str(m)] + " minute past " + num[str(h)]
            elif m == 15:
                res = "quarter past " + num[str(h)]
            elif m < 30:
                while m > 0:
                    if m > 20:
                        res += num["20"] + " "
                        m -= 20
                    elif m > 10:
                        res += num[str(m)] + " "
                        m -= m
                    else:
                        res += num[str(m)] + " "
                        m -= m
                res += "minutes past " + num[str(h)]
            else:
                if m == 59:
                    res = "one minute to " + num[str(h+1)]
                elif m == 30:
                    res = "half past " + num[str(h)]
                elif m == 45:
                    res = "quarter to " + num[str(h+1)]
                else:
                    h += 1
                    m = 60 - m
                    while m > 0:
                        if m > 20:
                            res += num["20"] + " "
                            m -= 20
                        elif m > 10:
                            res += num[str(m)] + " "
                            m -= m
                        else:
                            res += num[str(m)] + " "
                            m -= m
                    res += "minutes to " + num[str(h)]
            print(res)
