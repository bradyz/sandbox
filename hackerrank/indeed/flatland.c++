#include <cstdio>
#include <cstring>
#include <vector>

using namespace std;

#define UNVISITED 0

int V, E, P;

int dfs_low[100005];
int dfs_num[100005];
int dfs_parent[100005];

int dfsRoot;
int rootChildren;

int dfsNumberCounter;

vector<vector<int> > AdjList;

void findBridgeDFS(int u) {
    dfs_low[u] = dfs_num[u] = dfsNumberCounter++; // dfs_low[u] <= dfs_num[u]
    for (int v: AdjList[u]) {
        if (dfs_num[v] == UNVISITED) { // a tree edge
            printf("u: %d v: %d\n", u, v);
            dfs_parent[v] = u;
            if (u == dfsRoot) rootChildren++; // special case if u is a root
            findBridgeDFS(v);
            if (dfs_low[v] > dfs_num[u]) // for bridge
                printf("Edge (%d, %d) is a bridge\n", u, v);
            dfs_low[u] = min(dfs_low[u], dfs_low[v]); // update dfs_low[u]
        }
        else if (v != dfs_parent[u]) // a back edge and not direct cycle
            dfs_low[u] = min(dfs_low[u], dfs_num[v]); // update dfs_low[u]
    }
}

int main () {
    scanf("%d %d %d\n", &V, &E, &P);
    printf("%d %d %d\n", V, E, P);
    AdjList.resize(V+1);
    for (int i = 0; i < E; ++i) {
        int u, v;
        scanf("%d %d", &u, &v);
        AdjList[u].push_back(v);
        AdjList[v].push_back(u);
        printf("%d %d\n", u, v);
    }
    dfsNumberCounter = 0;
    memset(dfs_num, UNVISITED, V);
    memset(dfs_low, 0, V);
    memset(dfs_parent, 0, V);
    printf("Bridges:\n");
    for (int i = 1; i <= V; i++) {
        if (dfs_num[i] == UNVISITED) {
            dfsRoot = i; 
            rootChildren = 0; 
            findBridgeDFS(i);
        }
    }
    return 0;
}
