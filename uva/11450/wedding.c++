#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

int T;
int M, C;
int dp[205][25];
int garments[25][25];

int memo (int money, int clothing) {
    if (money < 0)
        return -1;
    else if (clothing == 0)
        return M - money;

    if (dp[money][clothing] > -1)
        return dp[money][clothing];

    int& ret = dp[money][clothing];

    for (int i = 1; i <= garments[clothing][0]; ++i)
        ret = max(ret, memo(money-garments[clothing][i], clothing-1));

    return ret;
}

int main () {
    cin >> T;
    while (T--) {
        cin >> M >> C;
        for (int c = 1; c <= C; ++c) {
            cin >> garments[c][0];
            for (int k = 1; k <= garments[c][0]; ++k)
                cin >> garments[c][k];
        }
        memset(dp, -1, sizeof(dp));
        int ret = memo(M, C);
        if (ret < 0)
            cout << "no solution" << endl;
        else
            cout << ret << endl;
    }
    return 0;
}
