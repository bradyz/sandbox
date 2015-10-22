#include <iostream>

using namespace std;

int main () {
    int coins[] = {2, 4, 7, 11, 15};
    int n = sizeof(coins) / sizeof(int);
    int v = 27;

    int dp[v+1][n+1];

    for (int i = 0; i <= v; ++i) {
        for (int j = 0; j <= n; ++j) {
            if (i == 0)
                dp[i][j] = 0;
            else if (j == 0)
                dp[i][j] = 999;
            else if (coins[j-1] > i)
                dp[i][j] = dp[i][j-1];
            else
                dp[i][j] = min(dp[i][j-1], dp[i-coins[j-1]][j]+1);
        }
    }

    for (int i = 0; i <= v; ++i) {
        for (int j = 0; j <= n; ++j)
            cout << dp[i][j] << "\t";
        cout << endl;
    }

    cout << dp[v][n] << endl;

    return 0;
}
