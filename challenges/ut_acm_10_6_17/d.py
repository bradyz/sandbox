def solve():
    spots = [i for i in range(n) if c[i] == 'E']
    spots_set = set(spots)

    for i in spots:
        can_cover = False

        for j in range(i-2, i+3):
            if j not in spots_set and j >= 0 and j < n:
                can_cover = True

        if not can_cover:
            return -1

    result = 0
    last = -3

    for i in spots:
        if last + 2 >= i:
            continue

        for j in [i+2, i+1]:
            if j not in spots_set:
                last = j
                result += 1
                break

        if last + 2 >= i:
            continue

        for j in [i-1, i-2]:
            if j not in spots_set:
                last = j
                result += 1
                break

    return result


n = int(input())
c = input()

print(solve())
