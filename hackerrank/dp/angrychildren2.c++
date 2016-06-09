#include <cstdio>
#include <algorithm>
#include <climits>

using namespace std;

int n, k;
unsigned long long c[100005];
unsigned long long p[100005];

int main () {
  scanf("%d%d", &n, &k);
  for (int i = 0; i < n; ++i) {
    scanf("%lld", c + i);
  }
  sort(c, c + n);
  p[0] = c[0];
  for (int i = 1; i < n; ++i) {
    p[i] = p[i-1] + c[i]; 
  }
  unsigned long long m = ULLONG_MAX;
  for (int j = 0; j < n-k+1; ++j) {
    unsigned long long total = 0;
    for (int i = 0; i < k-1; ++i) {
      total += (p[k-1+j] - p[i+j]) - (c[i+j] * (k - i - 1));
    }
    m = min(m, total);
  }
  printf("%lld\n", m);
}
