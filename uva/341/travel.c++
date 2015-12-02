#include <iostream>
#include <vector>
#include <utility>

using namespace std;

typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef long long ll;

int N, M;
int x, y;
ll dist[20][20];
int par[20][20];

void print (int i, int j) {
    if (i != j)
        print(i, par[i][j]);
    cout << j;
    if (j != y)
         cout << " ";
}

int main () {
    for (int t = 1; ; ++t) {
        cin >> N;
        if (N == 0)
            break;
        for (int i = 0; i <= N; ++i) {
            for (int j = 0; j <= N; ++j) {
                dist[i][j] = 1e9;
                par[i][j] = i;
            }
        }
        for (int u = 1; u <= N; ++u) {
            cin >> M;
            for (int m = 0; m < M; ++m) {
                int v, w;
                cin >> v >> w;
                dist[u][v] = w;
            }
        }
        for (int k = 1; k <= N; ++k) {
            for (int i = 1; i <= N; ++i) {
                for (int j = 1; j <= N; ++j) {
                    if (dist[i][j] > dist[i][k] + dist[k][j]) {
                        dist[i][j] = dist[i][k] + dist[k][j];
                        par[i][j] = par[k][j];
                    }
                }
            }
        }
        cin >> x >> y;
        cout << "Case " << t << ": Path = ";
        print(x, y);
        cout << "; " << dist[x][y] << " second delay" << endl;
    }
    return 0;
}
