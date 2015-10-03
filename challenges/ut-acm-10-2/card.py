v = ["01", "02", "03", "04" "05", "06", "07", "08", "09", "10", "11", "12"]

for i in range(int(input())):
    try:
        x, y = input().split()
        a = len(x) == 8
        b = int(x[0]) % 2 == 1
        c = y[:2] in v
        d = int(x) % int(y) == 0
        if a and b and c and d:
            print("Case " + str(i+1) + ": VALID")
        else:
            print("Case " + str(i+1) + ": BOGUS")
    except:
        print("Case " + str(i+1) + ": BOGUS")
