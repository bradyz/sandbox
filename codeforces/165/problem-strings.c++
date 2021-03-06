#include <iostream>
#include <string>

using namespace std;

long long dp[2 << 10];

int main() {
    int a;
    int j = 0;
    long long r = 0;
    string s;

    dp[0] = 1;

    cin >> a >> s;

    for(int i = 0; i < s.length(); ++i) {
        if(s[i] == '1')
            ++j;
        if(j >= a)
            r += dp[j-a];
        ++dp[j];
    }

    for(int i = 0; i < 2 << 10; ++i)
        cout << dp[i];

    // cout << r << endl;
}
