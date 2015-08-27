# O(n^3) as the list is turned into a set
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


# O(n^2) construction of adj_graph, O(V + E) for dfs
def solveV2(contact_list):
    def dfs(cur, parent):
        if used[cur]:
            return

        group[parent].append(cur)
        used[cur] = True

        for head in range(len(adj_graph)):
            if adj_graph[cur][head]:
                dfs(head, parent)

    adj_graph = [[False for j in contact_list] for i in contact_list]
    group = {i: [] for i in range(len(contact_list))}
    used = [False for _ in contact_list]

    for i in range(len(contact_list)):
        for j in range(i+1, len(contact_list)):
            if contact_list[i][0] == contact_list[j][0] or \
                    contact_list[i][0] == contact_list[j][1] or \
                    contact_list[i][0] == contact_list[j][2] or \
                    contact_list[i][1] == contact_list[j][0] or \
                    contact_list[i][1] == contact_list[j][1] or \
                    contact_list[i][1] == contact_list[j][2] or \
                    contact_list[i][2] == contact_list[j][0] or \
                    contact_list[i][2] == contact_list[j][1] or \
                    contact_list[i][2] == contact_list[j][2]:
                adj_graph[i][j] = True
                adj_graph[j][i] = True

    for i in range(len(contact_list)):
        dfs(i, i)

    for people in (g for g in group if group[g]):
        print(" ".join(map(str, group[people])))


if __name__ == "__main__":
    contacts = [tuple(input().split()) for _ in range(int(input()))]
    solveV2(contacts)
    solve(contacts)
