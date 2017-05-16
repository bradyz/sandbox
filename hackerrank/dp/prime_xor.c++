#include <iostream>
#include <cstring>
#include <vector>

using namespace std;

const int M = 9005;
const int N = 5005;
const int MOD = 1000000009;

int q;
int n;

vector<int> v;
int c[N];
int dp[M][N];
bool prime[M];

void sieve() {
  memset(prime, true, M * sizeof(bool));

  prime[0] = false;
  prime[1] = false;

  for (int i = 2; i < M; i++) {
    if (!prime[i])
      continue;

    for (int j = i + i; j < M; j += i)
      prime[j] = false;
  }
}

int waysToMake(int val, int pos) {
  if (val == 0 && pos == 0)
    return 1;
  else if (val != 0 && pos == 0)
    return 0;
  else if (val >= M)
    return 0;
  else if (dp[val][pos] != -1)
    return dp[val][pos];

  int save = 0;

  int x = waysToMake(val, pos - 1);
  int y = waysToMake(val ^ v[pos-1], pos - 1);

  int freq = c[v[pos-1]];

  int a = freq / 2 + 1;
  int b = (freq + 1) / 2;

  save += (a * x) % MOD;
  save += (b * y) % MOD;
  save %= MOD;

  return (dp[val][save] = save);
}

int solve() {
  int result = 0;

  for (int i = 0; i < M; i++) {
    if (prime[i])
      result += waysToMake(i, n) % MOD;
  }

  return result;
}

int main() {
  std::ios::sync_with_stdio(false);

  sieve();

  cin >> q;

  while (q--) {
    memset(c, 0, N * sizeof(int));
    memset(dp, -1, M * N * sizeof(int));
    v.clear();

    cin >> n;

    for (int i = 0; i < n; i++) {
      int tmp;
      cin >> tmp;

      c[tmp]++;
    }

    for (int i = 0; i < N; i++) {
      if (c[i] > 0)
        v.push_back(i);
    }

    cout << solve() << endl;
  }

  return 0;
}
