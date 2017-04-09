ALL = set("GIN, WHISKEY, RUM, TEQUILA, BOURBON, BRANDY, ABSINTHE, TRIPLESEC, LIQUER, VODKA, BARLEY, RYE, SAKE, COGNAC, MEZCAL".split(", "))

n = int(input())

left = set(ALL)
can = [set() for _ in range(n)]

for i in range(n):
    like = input().split(", ")
    dislike = input().split(", ")

    for drink in dislike:
        if drink in left:
            left.remove(drink)

    for drink in like:
        can[i].add(drink)

result = True

for i in range(n):
    found = False

    for drink in can[i]:
        if drink in left:
            found = True

    result = result and found

if result:
    print("its lit")
else:
    print("not lit")
