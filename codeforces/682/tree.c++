#include <cstdio>
#include <cstring>
#include <vector>
#include <utility>

using namespace std;

typedef pair<int, int> pii;

int n;
int keep = 0;
int a[100005];
vector<pii> g[100005];

void dfs (int u, long long d) {
  if (d > a[u])
    return;
  ++keep;
  for (pii& v : g[u]) {
    dfs(v.first, max(d + v.second, 0ll));
  }
}

int main () {
  scanf("%d", &n);
  for (int i = 1; i <= n; ++i) {
    scanf("%d", &a[i]);
  }
  for (int u = 2; u <= n; ++u) {
    int v, w;
    scanf("%d %d", &v, &w);
    g[v].push_back(pii(u, w));
  }
  dfs(1, 0ll);
  printf("%d\n", n - keep);
  return 0;
}
