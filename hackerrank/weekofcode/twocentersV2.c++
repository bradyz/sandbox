#include <iostream>
#include <queue>
#include <algorithm>
#include <cstring>

using namespace std;

int N;
vector<vector<int> > g(5010);
int dist[5010][5010];
bool vis[5010];

void bfs (int u, int d) {
    memset(vis, false, sizeof(vis));
    queue<int> q;
    q.push(u);
    vis[u] = true;
    dist[u][u] = 0;
    int level = 0;
    while (q.size() > 0) {
        ++level;
        int qsize = q.size();
        for (int i = 0; i < qsize; ++i) {
            int v = q.front();
            q.pop();
            for (int w: g[v]) {
                if (vis[w])
                    continue;
                vis[w] = true;
                dist[u][w] = level;
                dist[w][u] = level;
                q.push(w);
            }
        }
    }
}

int main () {
    cin >> N;
    memset(dist, -1, 5010 * 5010 * sizeof(int));
    for (int n = 0; n < N; ++n) {
        int u, v;
        cin >> u >> v;
        g[u].push_back(v);
        g[v].push_back(u);
    }
    for (int k = 1; k <= N; ++k)
        bfs(k, 0);
    int best = N;
    for (int i = 1; i <= N; ++i) {
        for (int j = i+1; j <= N; ++j) {
            int worst = -1;
            for (int u = 1; u <= N; ++u) {
                int tmp = min(dist[i][u], dist[j][u]);
                worst = max(worst, tmp);
            }
            best = min(best, worst);
        }
    }
    cout << best << endl;
    return 0;
}
