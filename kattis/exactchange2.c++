#include <iostream>

using namespace std;

typedef long long ll;

const ll INF = 1e9;

ll t, n, m;
int c[105];
int dp[20005][105];

void solve() {
  for (int i = 0; i < 20005; i++)
    for (int j = 0; j < 105; j++)
      dp[i][j] = INF;

  ll n_r = INF;
  ll dist_r = INF;
  ll count_r = INF;

  dp[0][0] = 0;

  for (int i = 0; i < 20005; i++) {
    for (int j = 1; j <= m; j++) {
      dp[i][j] = min(dp[i][j], dp[i][j-1]);

      if (i-c[j] >= 0)
        dp[i][j] = min(dp[i][j], dp[i-c[j]][j-1] + 1);

      if (i >= n && dp[i][j] < INF) {
        ll dist = abs(i - n);

        if (dist < dist_r || (dist == dist_r && dp[i][j] < count_r)) {
          n_r = i;
          dist_r = dist;
          count_r = dp[i][j];
        }
      }
    }

  }

  cout << n_r << " " << count_r << endl;
}

int main() {
  cin >> t;
  for (int i = 0; i < t; i++) {
    cin >> n;
    cin >> m;
    for (int j = 1; j <= m; j++)
      cin >> c[j];
    solve();
  }
  return 0;
}
