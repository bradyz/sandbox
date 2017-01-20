#include <vector>
#include <algorithm>

using namespace std;

int n, m;

int main () {
  while (true) {
    int x;
    scanf("%d %d", &n, &m);
    if (n == 0 && m == 0)
      break;
    vector<int> a;
    vector<int> b;
    for (int i = 0; i < n; i++) {
      scanf("%d", &x);
      a.push_back(x);
    }
    for (int i = 0; i < m; i++) {
      scanf("%d", &x);
      b.push_back(x);
    }
    int r = 0;
    int i = 0;
    int j = 0;
    while (i < a.size() && j < b.size()) {
      if (a[i] == b[j]) {
        x = a[i];
        r++;
        while (i < a.size() && a[i] == x)
          i++;
        while (j < b.size() && b[j] == x)
          j++;
      }
      else if (a[i] < b[j]) {
        i++;
      }
      else {
        j++;
      }
    }
    printf("%d\n", r);
  }
  return 0;
}
