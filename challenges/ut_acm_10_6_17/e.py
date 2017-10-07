def sorter(x):
    result = []

    result.append(x[0][0] in 'aeiou')
    result.append(int(x[2]))
    result.append(int(x[3]) in [6, 7, 8])
    result.append(-int(x[4]))
    result.append(x[1])

    return result


n = int(input())
people = [input().split() for _ in range(n)]

people.sort(key=sorter)

for val in people:
    print('%s %s' % (val[0], val[1]))
