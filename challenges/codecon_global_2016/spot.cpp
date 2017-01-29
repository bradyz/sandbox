#include <iostream>
#include <algorithm>
#include <vector>
#include <utility>

using namespace std;

typedef pair<int, int> pii;

int n, m;
vector<pair<pii, pii> > segments[105];

bool ccw(pii& A, pii &B, pii& C) {
  return (C.second-A.second) * (B.first-A.first) > (B.second-A.second) * (C.first-A.first);
}

bool intersect(pair<pii, pii> &a, pair<pii, pii> &b) {
  // cout << a.first.first << " " << a.first.second << endl;
  // cout << a.second.first << " " << a.second.second << endl;
  return ccw(a.first, b.first, b.second) != ccw(a.second, b.first, b.second) &&
    ccw(a.first, a.second, b.first) != ccw(a.first, a.second, b.second);
}

int main () {
  cin >> n >> m;
  for (int i = 0; i < n; i++) {
    int k;
    cin >> k;
    int t = 0;
    int x1, x2, y1, y2;
    for (int j = 0; j < k; j++) {
      cin >> y2;
      if (j != 0) {
        x1 = t;
        x2 = t + abs(y2 - y1);
        segments[i].push_back(pair<pii, pii>(pii(x1, y1), pii(x2, y2)));
        t += abs(y2 - y1);
      }
      y1 = y2;
    }
  }
  for (int i = 0; i < m; i++) {
    int u, v;
    cin >> u >> v;
    int r = 0;
    for (int j = 0; j < segments[u-1].size(); j++) {
      for (int k = 0; k < segments[v-1].size(); k++) {
        if (intersect(segments[u-1][j], segments[v-1][k]))
          r++;
      }
    }
    cout << r << endl;
  }
  return 0;
}
