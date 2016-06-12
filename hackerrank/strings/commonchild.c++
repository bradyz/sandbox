#include <iostream>
#include <string>

using namespace std;

int n;
string s, t;
int dp[5005][5005];

int main () {
  cin >> s;
  cin >> t;
  n = s.size();
  dp[0][0] = (s[0] == t[0]);
  for (int i = 1; i < n; ++i) {
    dp[i][0] = max(dp[i-1][0], (int) (s[i] == t[0]));
    dp[0][i] = max(dp[0][i-1], (int) (t[i] == s[0]));
  }
  for (int i = 1; i < n; ++i) {
    for (int j = 1; j < n; ++j) {
      dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
      if (s[i] == t[j])
        dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 1);
    }
  }
  int r = -1;
  for (int i = 0; i < n; ++i)
    for (int j = 0; j < n; ++j)
      r = max(r, dp[i][j]);
  cout << r << endl;
  return 0;
}
