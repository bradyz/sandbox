# 474B: Keyboard
# Start Time: 6:50 p.m. 5-1-15
# End Time: 7:00 p.m. 5-1-15

c = "qwertyuiopasdfghjkl;zxcvbnm,./"
d = -1 if input() == "R" else 1
print("".join(list(map(lambda x: c[c.index(x)+d], input()))))
