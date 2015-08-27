# O(n^3) because the list is turned into a set
def solve(contact_list):
    children = {i: [] for i in range(len(contact_list))}
    is_parent = [False for _ in range(len(contact_list))]

    for i in range(len(contact_list)):
        found = False
        for j in range(i+1, len(contact_list)):
            if not set(contact_list[i]).isdisjoint(set(contact_list[j])):
                children[j].append(i)
                is_parent[j] = False
                found = True
        if not found:
            is_parent[i] = True

    for parent in filter(lambda x: is_parent[x], children):
        print(" ".join(map(str, [parent] + children[parent])))


if __name__ == "__main__":
    contacts = [tuple(input().split()) for _ in range(int(input()))]
    solve(contacts)
