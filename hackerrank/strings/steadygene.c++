#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int n;
string s;
string T = "ACTG";
int pre[500005][4];
int extra[100];

int main () {
  cin >> n;
  cin >> s;
  for (int i = 1; i < n + 1; ++i) {
    for (int j = 0; j < T.size(); ++j) {
      pre[i][j] = pre[i-1][j] + (s[i-1] == T[j]);
    }
  }
  for (int i = 0; i < T.size(); ++i) {
    extra[i] = max(0, int(pre[n][i] - n / T.size()));
  }
  int best = int(1e9);
  for (int i = 0; i < n + 1; ++i) {
    int lo = i;
    int hi = n;
    int mi;
    while (lo < hi) {
      mi = (lo + hi) / 2;
      bool can = true;
      for (int j = 0; j < T.size(); ++j) {
        if (pre[mi][j] - pre[i][j] < extra[j])      
          can = false;
      }
      if (can)
        hi = mi;
      else
        lo = mi + 1;
    }
    mi = (lo + hi) / 2;
    bool can = true;
    for (int j = 0; j < T.size(); ++j) {
      if (pre[mi][j] - pre[i][j] < extra[j])      
        can = false;
    }
    if (can)
      best = min(best, mi - i);
  }
  cout << best << endl;
  return 0;
}
