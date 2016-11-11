#include <iostream>
#include <cstring>
#include <cmath>

using namespace std;

int T;
int n;
bool dp[50005][505];
int c[505];

void solve (int total) {
    for (int i = 0; i <= total; ++i)
        for (int j = 0; j <= n; ++j)
            dp[i][j] = false;
    for (int i = 0; i <= n; ++i)
        dp[0][i] = true;
    for (int i = 1; i <= total; ++i) {
        for (int j = 1; j <= n; ++j) {
            dp[i][j] = dp[i][j-1];
            if (i - c[j-1] >= 0)
                dp[i][j] |= dp[i - c[j-1]][j-1];
        }
    }
    int r = int(1e9);
    for (int i = 0; i <= total; ++i) {
        for (int j = 0; j <= n; ++j) {
            if (dp[i][j] && abs(i - (total - i)) <= abs(r - (total - r)))
                r = i;
        }
    }
    cout << abs(r - (total - r)) << endl;
}

int main () {
    cin >> T;
    while (T--) {
        cin >> n;
        int total = 0;
        for (int i = 0; i < n; ++i) {
            cin >> c[i];
            total += c[i];
        }
        solve(total);
    }
    return 0;
}
