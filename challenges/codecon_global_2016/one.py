def selection_sort(values):
    result = 0
    for i in range(len(values)-1, -1, -1):
        s_i = 0
        for j in range(i+1):
            if values[j] > values[s_i]:
                s_i = j
        if i != s_i:
            values[i], values[s_i] = values[s_i], values[i]
            result += 1
    return result

print(selection_sort([int(input()) for _ in range(int(input()))]))
