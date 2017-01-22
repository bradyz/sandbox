#include <iostream>
#include <cstring>

using namespace std;

int n;
int c[1005];
bool dp[2005][1005];

int main () {
  memset(dp, false, 2005 * 1005);

  cin >> n;
  for (int i = 0; i < n; i++)
    cin >> c[i];

  for (int i = 0; i < n; i++)
    dp[0][i] = true;

  dp[c[0]][0] = true;

  for (int i = 1; i < 2005; i++) {
    for (int j = 1; j < n; j++) {
      if (i - c[j] >= 0 && dp[i - c[j]][j-1])
        dp[i][j] = true;
      dp[i][j] |= dp[i][j-1];
    }
  }

  int r = 0;

  for (int i = 0; i < 2005; i++) {
    if (dp[i][n-1] && abs(1000 - i) <= abs(1000 - r))
      r = i;
  }

  cout << r << endl;

  return 0;
}
