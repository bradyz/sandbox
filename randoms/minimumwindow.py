import sys
from collections import Counter


def min_win(hay, ndl):
    req = Counter()
    has = Counter()
    beg = -1
    end = -1
    cur_beg = -1
    cur_end = -1

    for char in ndl:
        req[char] += 1

    ndl = set(ndl)

    for i, char in enumerate(hay):
        if char in ndl:
            has[char] += 1
            if beg == -1:
                beg = i
            elif has_required(req, has):
                end = i
                break

    cur_beg = beg
    cur_end = end

    while cur_end < len(hay):
        if has_required(req, has):
            if cur_end - cur_beg < end - beg:
                beg = cur_beg
                end = cur_end
            has[hay[cur_beg]] -= 1
            cur_beg += 1
        else:
            cur_end += 1
            if cur_end < len(hay):
                has[hay[cur_end]] += 1

    return hay[beg: end + 1]


def has_required(req_count, has_count):
    for x in req_count:
        if has_count[x] < req_count[x]:
            return False
    return True


if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        if i % 2 == 0:
            s = [char for char in line.strip("\n")]
        else:
            t = [char for char in line.strip("\n")]
            window = min_win(s, t)
            print(window)
