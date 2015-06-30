# Given an unsorted array, find the max j-i such that j > i and a[j] > a[i]
# in O(N).

c = [5, 3, 2, 4, 1, 2, 5]


def trivial(a):
    m_j, m_i = 0, 0
    n = len(a)
    for i in range(n):
        for j in range(i+1, n):
            if a[j] > a[i] and j - i > m_j - m_i:
                m_i, m_j = i, j
    print(m_i, m_j)

trivial(c)
