#include <iostream>
#include <cstring>

using namespace std;

int n;
int c[3];
int dp[4001][4001];

int main () {
    memset(dp, -1, sizeof(int)*4001*4001);
    cin >> n >> c[0] >> c[1] >> c[2];
    for (int i = 0; i <= n; ++i) {
        for (int j = 0; j <= 3; ++j) {
            if (i == 0)
                dp[i][j] = 0;
            else if (j == 0)
                continue;
            else if (i-c[j-1] >= 0 && dp[i-c[j-1]][j] != -1)
                dp[i][j] = max(dp[i-c[j-1]][j]+1, dp[i][j-1]);
            else
                dp[i][j] = dp[i][j-1];
        }
    }
    cout << dp[n][3] << endl;
    return 0;
}
