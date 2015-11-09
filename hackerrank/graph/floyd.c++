#include <iostream>
#include <climits>

using namespace std;

int N, M;
int Q;
long long dist[401][401];

int main () {
    cin >> N >> M;
    for (int i = 1; i <= N; ++i)
        for (int j = 1; j <= N; ++j)
            dist[i][j] = INT_MAX;
    for (int i = 1; i <= N; ++i)
        dist[i][i] = 0;
    for (int m = 0; m < M; ++m) {
        int u, v;
        long long w;
        cin >> u >> v >> w;
        dist[u][v] = w;
    }
    for (int k = 1; k <= N; ++k)
        for (int i = 1; i <= N; ++i)
            for (int j = 1; j <= N; ++j)
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j]);
    cin >> Q;
    for (int q = 0; q < Q; ++q) {
        int u, v;
        cin >> u >> v;
        if (dist[u][v] < INT_MAX)
            cout << dist[u][v] << endl;
        else
            cout << -1 << endl;
    }
    return 0;
}
