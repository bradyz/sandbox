#include <iostream>
#include <queue>
#include <vector>
#include <cstring>

using namespace std;

typedef pair<int, int> ii;
typedef vector<ii> vii;

int T;
int N, M;
int S;
bool vis[1010];
int dist[1010];

int main () {
    cin >> T;
    while (T--) {
        cin >> N >> M;
        vector<vector<int> >graph(N+1);
        queue<int> que;
        memset(vis, false, sizeof vis);
        memset(dist, -1, sizeof dist);
        for (int m = 0; m < M; ++m) {
            int u, v;
            cin >> u >> v;
            graph[u].push_back(v);
            graph[v].push_back(u);
        }
        cin >> S;
        int level = 0;
        que.push(S);
        vis[S] = true;
        while (que.size() > 0) {
            int size = que.size();
            for (int s = 0; s < size; ++s) {
                int u = que.front();
                que.pop();
                dist[u] = level;
                for (int v: graph[u]) {
                    if (vis[v]) 
                        continue;
                    vis[v] = true;
                    que.push(v);
                }
            }
            ++level;
        }
        for (int u = 1; u <= N; ++u) {
            if (u == S)
                continue;
            if (dist[u] == -1)
                cout << dist[u];
            else
                cout << dist[u] * 6;
            if (u != N)
                cout << " ";
        }
        cout << endl;

    }
    return 0;
}
