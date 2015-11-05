#include <iostream>
#include <algorithm>
#include <climits>

using namespace std;

int T;
int L;
int S;
int strategy[1001];
long long cost[1001][10];
long long health[1001][10];
long long dp[1001][101];

int main () {
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cin >> L;
        for (int l = 1; l <= L; ++l) {
            cin >> strategy[l];
            for (int s = 0; s < strategy[l]; ++s) {
                int n, h;
                cin >> n >> h;
                cost[l][s] = n;
                health[l][s] = h;
            }
        }
        for (int l = 0; l <= L; ++l)
            for (int h = 0; h <= 100; ++h)
                dp[l][h] = INT_MAX;
        dp[0][100] = 0;
        for (int l = 0; l < L; ++l) {
            for (int h = 1; h <= 100; ++h) {
                if (dp[l][h] == INT_MAX) continue;
                for (int s = 0; s < strategy[l+1]; ++s) {
                    if (h - health[l+1][s] <= 0)
                        continue;
                    else if (h - health[l+1][s] >= 100)
                        dp[l+1][100] = min(dp[l][h]+cost[l+1][s], dp[l+1][100]);
                    else {
                        int h1 = h - health[l+1][s];
                        dp[l+1][h1] = min(dp[l][h]+cost[l+1][s], dp[l+1][h1]);
                    }
                }
            }
        }
        long long best = INT_MAX;
        for (int i = 1; i <= 100; ++i)
            best = min(best, dp[L][i]);
        if (best == INT_MAX)
            cout << "Case " << t << ": IMPOSSIBLE" << endl;
        else
            cout << "Case " << t << ": " << best << endl;
    }
    return 0;
}
