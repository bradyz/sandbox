#include <iostream>
#include <vector>

using namespace std;

int t, n, m;
int u, v;

vector<int> g[100005];
double memo[100005];

double solve(int x) {
    if (memo[x] > 0.0)
        return memo[x];
    else if (x == n)
        return 0.0;
    double result = 0.0;
    for (int y : g[x])
        result += solve(y);
    memo[x] = result / g[x].size() + 1.0;
    return memo[x];
}

int main() {
    cin >> t;
    while(t--) {
        cin >> n >> m;
        for (int i = 1; i <= n; i++) {
            g[i].clear();
            memo[i] = -1.0;
        }
        for (int i = 0; i < m; i++) {
            cin >> u >> v;
            g[u].push_back(v);
        }
        printf("%.3f\n", solve(1));
    }
}
