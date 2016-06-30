#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;

int n, m;
vector<int> g[1000005];
int color[1000005];
bool vis[1000005];

bool bfs (int x) {
  color[x] = 1;
  vis[x] = true;
  queue<int> q;
  q.push(x);
  while (q.size() > 0) {
    int u = q.front();
    q.pop();
    for (int v : g[u]) {
      if (color[v] == color[u])
        return false;
      else if (vis[v])
        continue;
      vis[v] = true;
      color[v]= 1 - color[u];
      q.push(v);
    }
  }
  return true;
}

int main () {
  cin >> n >> m;
  for (int i = 0; i < m; ++i) {
    int u, v;
    cin >> u >> v;
    g[u].push_back(v);
    g[v].push_back(u);
  }
  memset(color, -1, sizeof color);
  memset(vis, 0, sizeof vis);
  bool can = true;
  for (int i = 1; i <= n; ++i) {
    if (vis[i])
      continue;
    can &= bfs(i);
  }
  if (can == false) {
    cout << -1 << endl;
  }
  else {
    vector<int> a;
    vector<int> b;
    for (int i = 1; i <= n; ++i) {
      if (color[i] == 1)
        a.push_back(i);
      else
        b.push_back(i);
    }
    cout << a.size() << endl;
    for (int i : a) cout << i << " ";
    cout << endl;
    cout << b.size() << endl;
    for (int i : b) cout << i << " ";
    cout << endl;
  }
}
