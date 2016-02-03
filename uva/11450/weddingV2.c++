#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

int T;
int M, C;
bool dp[205][25];
int garments[25][25];

int main () {
    cin >> T;
    while (T--) {
        cin >> M >> C;
        for (int c = 1; c <= C; ++c) {
            cin >> garments[c][0];
            for (int k = 1; k <= garments[c][0]; ++k)
                cin >> garments[c][k];
        }
        memset(dp, false, sizeof dp);
        dp[0][0] = true;
        for (int money = 0; money <= M; ++money) {
            for (int clothes = 1; clothes <= C; ++clothes) {
                for (int i = 1; i <= garments[clothes][0]; ++i) {
                    int after = money - garments[clothes][i];
                    if (after < 0 || !dp[after][clothes-1])
                        continue;
                    dp[money][clothes] = true;
                }
            }
        } 
        int ret = -1;
        for (int money = 0; money <= M; ++money) {
            if (dp[money][C])
                ret = money;
        }
        if (ret < 0)
            cout << "no solution" << endl;
        else
            cout << ret << endl;
    }
    return 0;
}
