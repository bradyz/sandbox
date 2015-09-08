def solve(w):
    if w == "".join(reversed(w)):
        return w[:len(w)//2] + w[len(w)//2] + w[len(w)//2:]

    for v in (w, "".join(reversed(w))):
        i, j, c = 0, len(w)-1, -1

        while i < j:
            if v[i] != v[j]:
                if c != -1:
                    i, j, c = -1, -1, -1
                    break
                else:
                    c = j
                    i += 1
            else:
                i += 1
                j -= 1

        if c != -1:
            return v[:c+1] + v[len(v)-1-c] + v[c+1:]

    return "NA"

print(solve(input()))
