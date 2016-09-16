#include <iostream>
#include <cstring>

using namespace std;

int dp[10000107][105];
int h[105];
int t;
int n;
int b;
int m;

int main () {
    cin >> t;
    while (t--) {
        cin >> n >> b >> m;
        for (int i = 0; i < m; ++i)
            cin >> h[i];
        for (int i = 0; i <= n; ++i)
            for (int j = 0; j < m; ++j)
                dp[i][j] = int(1e9);
        for (int i = 0; i < m; ++i)
            dp[0][i] = 0;
        for (int i = 0; i <= n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (h[j] > i)
                    continue;
                dp[i][j] = min(dp[i][j], dp[i-h[j]][j] + 1);
                if (j > 0)
                    dp[i][j] = min(dp[i][j], dp[i][j-1]);
            }
        }
    }
    return 0; 
}
