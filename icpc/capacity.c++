#include <iostream>
#include <algorithm>

using namespace std;

int T;
int N, K;
int value[1001];
int weight[1001];
int dp[1001][1001];

int solve () {
    for (int i = 0; i <= K; ++i)
        for (int j = 0; j <= N; ++j)
            dp[i][j] = 0;
    for (int i = 0; i <= K; ++i) {
        for (int j = 0; j <= N; ++j) {
            if (i == 0 || j == 0)
                continue;
            else if (i >= weight[j-1])
                dp[i][j] = max(dp[i][j-1], dp[i-weight[j-1]][j-1]+value[j-1]);
            else 
                dp[i][j] = dp[i][j-1];
        }
    }
    return dp[K][N];
}

int main () {
    cin >> T;
    for (int t = 0; t < T; ++t) {
        cin >> N >> K;
        for (int i = 0; i < N; ++i) {
            cin >> weight[i];
            cin >> value[i];
        }
        cout << solve() << endl;
    }
    return 0;
}
