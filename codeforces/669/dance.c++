#include <cstdio>

using namespace std;

int n, q;
int qt, d;
int p[1000005];

int main () {
  scanf("%d %d", &n, &q);
  int e = 0;
  int o = 0;
  while (q--) {
    scanf("%d", &qt);
    if (qt == 1) {
      scanf("%d", &d);
      e = (e + d) % n;
      o = (o + d) % n;
    }
    else if (qt == 2) {
      if (o % 2 == 0) {
        o = (o + 1) % n; 
        e = (e - 1) % n;
      }
      else {
        o = (o - 1) % n; 
        e = (e + 1) % n;
      }
    }
  }
  for (int i = 0; i < n; ++i) {
    if (i % 2 == 0)
      p[(i+o+n) % n] = i + 1;
    else
      p[(i+e+n) % n] = i + 1;
  }
  for (int i = 0; i < n; ++i)
    printf("%d ", p[i]);
  printf("\n");
  return 0;
}
