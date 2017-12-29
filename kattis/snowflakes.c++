#include <iostream>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;

int t, n;
vector<int> c;

void solve() {
  int l = 0;
  int r = 1;

  set<int> s;
  s.insert(c[0]);

  int result = 1;

  while (r < n) {
    while (s.find(c[r]) != s.end()) {
      s.erase(c[l]);
      l++;
    }

    s.insert(c[r]);
    r++;

    result = max(result, (int) s.size());
  }

  cout << result << endl;
}

int main() {
  cin >> t;

  while (t--) {
    c.clear();

    cin >> n;

    for (int i = 0; i < n; i++) {
      int tmp;
      cin >> tmp;
      c.push_back(tmp);
    }

    solve();
  }
  return 0;
}
