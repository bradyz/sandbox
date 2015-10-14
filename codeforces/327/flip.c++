#include <iostream>

using namespace std;

int n;
int t;
int r;
int dp[101];

int main () { 
    r = 0;

    cin >> n;

    for (int i = 0; i < n; ++i) {
        cin >> t;
        if (t == 0)
            dp[i] = 1;
        else {
            dp[i] = -1;
            r += 1;
        }
    }

    int c = 0;

    for (int i = 0; i < n; ++i) {
        c += dp[i];         
        dp[i] = max(dp[i], c);
        if (c < 0)
            c = 0;
    }

    c = -1;

    for (int i = 0; i < n; ++i)
        c = max(c, dp[i]);

    // for (int i = 0; i < n; ++i)
    //     cout << dp[i] << " ";
    // cout << endl;
    
    cout << r + c << endl;

    return 0;
}
