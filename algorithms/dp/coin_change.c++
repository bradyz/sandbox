#include <iostream>
#include <vector>

using namespace std;

int coins[] = {2, 4, 7, 11, 15};
int n = 5;
int v = 27;
int dp[28][6];


vector<int> findSolution (int v, int n) {
    vector<int> result;
    int j = n;

    while (v > 0 && j > 0) {
        if (dp[v][j] == dp[v][j-1])
            j -= 1;
        else {
            result.push_back(coins[j-1]);
            v -= coins[j-1];
        }
    }

    return result;
}

int main () {
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

    vector<int> result = findSolution(v, n);

    for (auto it: result)
        cout << it << " ";
    cout << endl;

    return 0;
}
