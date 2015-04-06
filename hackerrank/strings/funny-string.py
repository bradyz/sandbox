for _ in range(int(input())):
    a = input()
    funny = True
    for i in range(1, len(a)):
        if abs(ord(a[i])-ord(a[i-1])) != abs(ord(a[len(a)-1-i])-ord(a[len(a)-i])):
            funny = False
            break
    if funny:
        print("Funny")
    else:
        print("Not Funny")
