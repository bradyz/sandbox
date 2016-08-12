#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>

using namespace std;

int n;
int c[100005];
string s[100005][2];
bool can[100005][2];
int dp[100005][2];

int main () {
    memset(c, 0, sizeof c);
    memset(dp, int(1e9), sizeof dp);
    memset(can, 0, sizeof can);
    cin >> n;
    for (int i = 0; i < n; ++i) {
        cin >> c[i];
    }
    for (int i = 0; i < n; ++i) {
        cin >> s[i][0];
        s[i][1] = s[i][0];
        reverse(s[i][1].begin(), s[i][1].end());
    }
    can[0][0] = true;
    can[0][1] = true;
    dp[0][0] = 0;
    dp[0][1] = c[0];
    for (int i = 1; i < n; ++i) {
        if (!can[i-1][0] && !can[i-1][1])
            break;
        if (can[i-1][0]) {
            if (s[i][0] > s[i-1][0])
                dp[i][0] = min(dp[i][0], dp[i-1][0]);
            if (s[i][1] > s[i-1][0])
                dp[i][0] = min(dp[i][0], dp[i-1][0] + c[i]);
        }
        if (can[i-1][1]) {
            if (s[i][0] > s[i-1][1])
                dp[i][1] = min(dp[i][1], dp[i-1][1]);
            if (s[i][1] > s[i-1][1])
                dp[i][1] = min(dp[i][1], dp[i-1][1] + c[i]);
        }
    }
    for (int i = 0 ; i < n; ++i)
        cout << dp[i][0] << " " << dp[i][1] << endl;
    if (can[n-1][0] || can[n-1][2])
        cout << min(dp[n-1][0], dp[n-1][1]) << endl;
    else
        cout << -1 << endl;
    return 0;
}
