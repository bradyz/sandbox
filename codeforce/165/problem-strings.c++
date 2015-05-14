#include <iostream>
#include <string>
#include <string.h>

using namespace std;


int main() {
    long long dp[21 << 2];
    int a;
    int j = 0;
    long long r = 0;
    string s;

    memset(dp, 0, sizeof(dp));
    dp[0] = 1;

    cin >> a >> s;

    for(int i = 0; i < s.length(); ++i) {
        if(s[i] == '1')
            ++j;
        if(j >= a)
            r += dp[j-a];
        ++dp[j];
    }

    cout << r << endl;
}
