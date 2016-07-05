#include <cstdio>

using namespace std;

#define N 17

int n, m;
int a[(1 << (N + 1)) + 1];

int main () {
  scanf("%d %d", &n, &m);
  for (int i = 0; i < (1 << n); ++i) {
    scanf("%d", &a[(1 << n) + i]);
  }
  for (int i = n-1, isXor = false; i >= 0; --i, isXor = !isXor) {
    for (int j = 0; j < (1 << i); ++j) {
      if (isXor)
        a[(1 << i) + j] = a[(1 << (i + 1)) + 2 * j] ^ a[(1 << (i + 1)) + 2 * j + 1];
      else
        a[(1 << i) + j] = a[(1 << (i + 1)) + 2 * j] | a[(1 << (i + 1)) + 2 * j + 1];
    }
  }
  for (int i = 0; i < m; ++i) {
    int p, b;
    scanf("%d %d", &p, &b);
    a[(1 << n) + p - 1] = b;
    for (int c = ((1 << n) + p - 1) >> 1, isXor = false; c > 0; c >>= 1, isXor = !isXor) {
      if (isXor)
        a[c] = a[2 * c] ^ a[2 * c + 1];
      else
        a[c] = a[2 * c] | a[2 * c + 1];
    }
    printf("%d\n", a[1]);
  }
  return 0;
}
