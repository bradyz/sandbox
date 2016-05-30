#include <cstring>
#include <iostream>
#include <map>

using namespace std;

int n;
int c[5005];
int r[5005];
int p[5005];

int main () {
  memset(p, -1, sizeof p);
  cin >> n;
  for (int i = 0; i < n; ++i) {
    cin >> c[i];
    if (p[c[i]] == -1) {
      p[c[i]] = i;
    }
  }
  // for (int i = 1; i <= n; ++i)
  //   cout << p[i] << " ";
  // cout << endl;
  for (int i = 0; i < n; ++i) {
    int o[5005];
    memset(o, 0, sizeof o);
    o[c[i]] = 1;
    r[c[i]] += 1;
    int mO = c[i];
    // for (int i = 1; i <= n; ++i)
    //   cout << o[i] << " ";
    // cout << endl;
    // cout << mO << endl;
    for (int j = i + 1; j < n; ++j) {
      o[c[j]] += 1;
      if (o[c[j]] >= o[mO]) {
        // cout << "test " << c[j] << " " << o[c[j]] << " idx: " << p[c[j]] << endl;
        // cout << "best " << mO << " " << o[mO] << " idx: " << p[mO] << endl;
        if (o[c[j]] > o[mO] || p[c[j]] < p[mO]) {
          // cout << "yes" << endl;
          mO = c[j];
        }
      }
      r[mO] += 1;
      // for (int i = 1; i <= n; ++i)
      //   cout << o[i] << " ";
      // cout << endl;
      // cout << mO << endl;
    }
    // cout << endl;
  }
  for (int i = 1; i <= n; ++i)
    cout << r[i] << " ";
  cout << endl;
}
