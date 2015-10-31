#include <iostream>
#include <limits.h>
#include <string.h>
#include <queue>
#include <algorithm>

using namespace std;

int N, M;
int r[2002][2002];
int parent[2002];
bool visited[2002];

bool bfs () {
    for (int i = 1; i <= N+M+1; ++i)
        visited[i] = false;
    queue <int> q;
    for (int s = 1; s <= N; ++s) {
        q.push(s);
        visited[s] = true;
        parent[s] = -1;
    }
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (int v = N+1; v <= N+M+1; v++) {
            if (visited[v]==false && r[u][v] > 0) {
                q.push(v);
                parent[v] = u;
                visited[v] = true;
                // we have hit the sink
                if (v == N+M+1)
                    return true;
            }
        }
    }
    return false;
}
 
int fordFulkerson () {
    int max_flow = 0;
    while (bfs()) {
        int path_flow = INT_MAX;
        for (int v = N+M+1; parent[v] != -1; v = parent[v]) {
            path_flow = min(path_flow, r[parent[v]][v]);
        }
        for (int v = N+M+1; parent[v] != -1; v = parent[v]) {
            r[parent[v]][v] -= path_flow;
            r[v][parent[v]] += path_flow;
        }
        // for (int i = 1; i <= N; ++i) {
        //     for (int j = N+1; j <= N+M; ++j) {
        //         cout << r[i][j] << "\t";
        //     }
        //     cout << endl;
        // }
        // cout << endl;
        max_flow += path_flow;
    }
    return max_flow;
}

int main () {
    int T;
    cin >> T;
    for (int t = 0; t < T; ++t) {
        cin >> N >> M;
        // clear graph
        for (int i = 1; i <= N+M+1; ++i) {
            for (int j = 1; j <= N+M+1; ++j)
                r[i][j] = 0;
        }
        for (int u = 1; u <= N; ++u) {
            int k;
            cin >> k;
            for (int i = 0; i < k; ++i) {
                int v;
                cin >> v;
                v += N;
                r[u][v] = 1;
                r[v][N+M+1] = 1;
            }
        }
        cout << fordFulkerson() << endl;
    }
    return 0;
}
