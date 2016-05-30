#include <cstring>
#include <iostream>
#include <map>

using namespace std;

int n;
int c[5005];
int r[5005];
int o[5005];

int main () {
  cin >> n;
  for (int i = 0; i < n; ++i) {
    cin >> c[i];
  }
  for (int i = 0; i < n; ++i) {
    memset(o, 0, sizeof o);
    o[c[i]] = 1;
    r[c[i]] += 1;
    int mO = c[i];
    for (int j = i + 1; j < n; ++j) {
      o[c[j]] += 1;
      if (o[c[j]] > o[mO] || (o[c[j]] == o[mO] && c[j] < mO)) {
        mO = c[j];
      }
      r[mO] += 1;
    }
  }
  for (int i = 1; i <= n; ++i)
    cout << r[i] << " ";
  cout << endl;
}
