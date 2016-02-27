#include <iostream>
#include <cstring>
#include <utility>
#include <vector>
#include <map>

#define pop_b pop_back
#define push_b push_back

using namespace std;

typedef pair<int, int> pii;

int T;
int N;
char g[1005][1005];
int dp[1005][1005];

int main () {
    cin >> T;
    while (T--) {
        cin >> N;
        for (int i = 0; i < N; ++i)
            cin >> g[i];
        memset(dp, 0, sizeof dp);
        vector<pii> s;
        map<int, int> r;
        for (int i = 1; i < N; ++i) {
            for (int j = 1; j < N; ++j) {
                if (g[i][j] == '1' && g[i-1][j] == '1' && 
                        g[i][j-1] == '1' && g[i-1][j-1] == '1') {
                    dp[i][j] = 2;
                    s.push_b(pii(i, j));
                    ++r[2];
                }
            }
        }
        int k = 3;
        while (s.size() > 0) {
            vector<pii> ns; 
            while (s.size() > 0) {
                int i = s.back().first;
                int j = s.back().second;
                s.pop_b();
                if (dp[i-1][j] >= k-1 && dp[i][j-1] >= k-1 && 
                        dp[i-1][j-1] >= k-1) {
                    dp[i][j] = k;
                    ns.push_b(pii(i, j));
                    ++r[k];
                }
            }
            s = ns;
            ++k;
        }
        for (auto it: r)
            cout << it.first << " " << it.second << endl;
    }
    return 0;
}
