#include <cstdio>
#include <algorithm>

using namespace std;

typedef unsigned long long ull;

int n;
int t, k;
int q[100005][2];
ull dp1[100005][2];
ull dp2[100005];

int main () {
  scanf("%d %d", &t, &k);
  for (int i = 0; i < t; ++i) {
    scanf("%d %d", &q[i][0], &q[i][1]);
    n = max(n, max(q[i][0], q[i][1]) + 1);
  }
  dp1[1][0] = 1;
  dp1[k][1] = 1;
  for (int i = 1; i < n; ++i) {
    if (i > 1)
      dp1[i][0] = dp1[i-1][0] + dp1[i-1][1];
    if (i > k)
      dp1[i][1] = dp1[i-k][0] + dp1[i-k][1];
    dp1[i][0] = dp1[i][0] % 1000000007;
    dp1[i][1] = dp1[i][1] % 1000000007;
    dp2[i] = (dp1[i][0] + dp1[i][1] + dp2[i-1]);
  }
  for (int i = 0; i < t; ++i)
    printf("%llu\n", (dp2[q[i][1]] - dp2[q[i][0]-1]) % 1000000007);
  return 0;
}
