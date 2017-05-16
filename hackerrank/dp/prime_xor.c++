#include <iostream>
#include <cstring>
#include <vector>

using namespace std;

typedef long long ll;

const int M = 8192;
const int N = 5005;
const int MOD = 1000000009;

int q;
int n;

bool prime[M];
int c[N];
ll dp[M][N];

void sieve() {
  prime[0] = false;
  prime[1] = false;

  for (int i = 2; i < M; i++) {
    for (int j = i + i; j < M; j += i)
      prime[j] = false;
  }
}

int even(int x) {
  return x / 2 + 1;
}

int odd(int x) {
  return (x + 1) / 2;
}

int solve() {
  for (int i = 0; i < 4500; i++)
    for (int j = 0; j < M; j++)
      dp[j][i] = 0;

  dp[0][3499] = 1;

  for (int i = 3500; i <= 4500; i++) {
    for (int j = 0; j < M; j++) {
      int amt = c[i];
      ll old = dp[j][i-1];

      dp[j][i] += even(amt) * old;
      dp[j][i] %= MOD;

      dp[i ^ j][i] += odd(amt) * old;
      dp[i ^ j][i] %= MOD;
    }
  }

  int result = 0;

  for (int i = 0; i < M; i++) {
    if (prime[i]) {
      result = (result + dp[i][4500]) % MOD;
    }
  }

	return result;
}

int main() {
  std::ios::sync_with_stdio(false);

  memset(prime, true, M * sizeof(bool));
  sieve();

  cin >> q;

  while (q--) {
    memset(c, 0, N * sizeof(int));
    memset(dp, 0, M * N * sizeof(ll));

    cin >> n;

    for (int i = 0; i < n; i++) {
      int tmp;
      cin >> tmp;

      c[tmp]++;
    }

    cout << solve() << endl;
  }

  return 0;
}
