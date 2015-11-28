#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

int N;
int g[5010][5010];

int main () {
    cin >> N;
    memset(g, -1, 5010 * 5010 * sizeof(int));
    for (int n = 0; n < N; ++n) {
        int u, v;
        cin >> u >> v;
        g[u][v] = 1;
        g[v][u] = 1;
    }
    for (int u = 1; u <= N; ++u)
        g[u][u] = 0;
    for (int k = 1; k <= N; ++k) {
        for (int i = 1; i <= N; ++i) {
            for (int j = 1; j <= N; ++j) {
                if (g[i][k] == -1 || g[k][j] == -1)
                    continue;
                else if (g[i][j] == -1)
                    g[i][j] = g[i][k] + g[k][j];
                else
                    g[i][j] = min(g[i][j], g[i][k] + g[k][j]);
            }
        }
    }
    int best = N;
    for (int i = 1; i <= N; ++i) {
        for (int j = i+1; j <= N; ++j) {
            int worst = -1;
            for (int u = 1; u <= N; ++u) {
                int tmp = min(g[i][u], g[j][u]);
                worst = max(worst, tmp);
            }
            best = min(best, worst);
        }
    }
    cout << best << endl;
    return 0;
}
