// 489C: Given Length and Sum of Digits
// Start: 3:55 p.m. 4-29-15
// End: 8:39 p.m. 4-29-15

#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int a, b;
    vector<vector<vector<int> > > dp(101, vector<vector<int> >(901, vector<int>()));
    vector<vector<vector<int> > > dp1(101, vector<vector<int> >(901, vector<int>()));
    vector<vector<bool> > v(101, vector<bool>(901, false));
    vector<vector<bool> > v1(101, vector<bool>(901, false));

    cin >> a >> b;

    for(int i = 0; i <= a; ++i) {
        for(int j = 0; j <= b; ++j) {
            for(int k = 0; k <= 9; ++k) {
                if(i == 0 && j == 0)
                    v[i][j] = v1[i][j] = true;
                else if(i == 0 || j == 0)
                    v[i][j] = v1[i][j] = false;
                else if(j - k >= 0) {
                    if(v[i-1][j-k] && !v[i][j]) {
                        v[i][j] = true;
                        dp[i][j] = dp[i-1][j-k];
                        dp[i][j].push_back(k);
                    }


                    if(v1[i-1][j-k] == 1) {
                        if(v[i][j] && dp1[i][j].size() > 0 && dp1[i][j].back() > k)
                            dp1[i][j].back() = k;
                        v1[i][j] = true;
                        dp1[i][j] = dp1[i-1][j-k];
                        dp1[i][j].push_back(k);
                    }
                }
            }
        }
    }

    if(a == 1 && b == 0)
        cout << "0 0" << endl;
    else if(v[a][b] == false)
        cout << "-1 -1" << endl;
    else {
        for(int i = 0; i < dp1[a][b].size(); ++i) 
            cout << dp1[a][b][i];

        cout << " ";

        for(int i = 0; i < dp[a][b].size(); ++i) 
            cout << dp[a][b][i];

        cout << endl;
    }

    return 0;
}
