#include <iostream>
#include <climits>
#include <cstring>

using namespace std;

int T;
int N, M, K;
int dp[31][31][51];

int memo (int n, int m, int k) {
    if (k == 0 || n * m == k)
        return 0;
    else if (dp[n][m][k] != -1)
        return dp[n][m][k];
    else if (n * m < k)
        return 1e9;
    int best = 1e9;
    for (int np = 1; np < n; ++np)
        for (int kp = 0; kp <= k; ++kp)
            best = min(best, m * m + memo(np, m, kp) + memo(n-np, m, k-kp));
    for (int mp = 1; mp < m; ++mp)
        for (int kp = 0; kp <= k; ++kp)
            best = min(best, n * n + memo(n, mp, kp) + memo(n, m-mp, k-kp));
    dp[n][m][k] = best;
    return best;
}

int main () {
    memset(dp, -1, sizeof(dp));
    cin >> T;
    for (int t = 0; t < T; ++t) {
        cin >> N >> M >> K;
        cout << memo(N, M, K) << endl;
    }
    return 0;
}
