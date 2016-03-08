#include <iostream>
#include <cstring>

using namespace std;

char g[55][55];
bool dp[55][55][55];

int t;
int n, m;

int main () {
    cin >> t;
    while (t--) {
        cin >> n >> m;
        for (int i = 0; i < n; ++i)
            cin >> g[i];
        memset(dp, false, sizeof dp);
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (i == 0 || j == 0 || i == n-1 || j == m-1)
                    continue;
                else if (g[i][j] != '1' ||
                         g[i-1][j] != '1' || g[i+1][j] != '1' ||
                         g[i][j-1] != '1' || g[i][j+1] != '1')
                    continue;
                dp[i][j][1] = true;
            }
        }
        for (int k = 2; k <= 50; ++k) {
            for (int i = 0; i < n; ++i) {
                for (int j = 0; j < m; ++j) {
                    if (i == 0 || j == 0 || i == n-1 || j == m-1)
                        continue;
                    else if (!dp[i][j][1] || 
                             !dp[i-1][j][k-1] || !dp[i+1][j][k-1] ||
                             !dp[i][j-1][k-1] || !dp[i][j+1][k-1])
                        continue;
                    dp[i][j][k] = true;
                }
            }
        }
        int ret = 0;
        for (int k = 50; k >= 1 && ret == 0; --k) {
            for (int i = 0; i < n && ret == 0; ++i) {
                for (int j = 0; j < m && ret == 0; ++j) {
                    if (dp[i][j][k])
                        ret = 1 + 2 * k;
                }
            }
        }
        cout << ret << endl;
        // for (int i = 0; i < n; ++i) {
        //     for (int j = 0; j < m; ++j)
        //         cout << dp[i][j][2] << " ";
        //     cout << endl;
        // }
    }
    return 0;
}
