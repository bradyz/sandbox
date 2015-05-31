// 313B: Ilya Queries
// Start Time: 12:46 a.m. 4-28-15
// End Time: 1:59 a.m. 4-28-15

#include <iostream>
#include <string>

using namespace std;

int main() {
    string asdf;
    getline(cin, asdf);

    int *dp = new int[asdf.length()];

    for(int i = 0; i < asdf.length(); ++i) {
        if(i == 0)
            dp[i] = 0;
        else
            dp[i] = dp[i-1] + (asdf[i] == asdf[i-1]);
    }

    int t;
    int a, b;

    cin >> t;

    while(t--) {
        cin >> a >> b;
        cout << dp[b-1] - dp[a-1] << endl;
    }

    delete dp;
}
