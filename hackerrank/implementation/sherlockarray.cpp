#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

#define fore(i, l, r) for(int i = (l); i < (r); ++i)
#define forn(i, n) fore(i, 0, n)
#define fori(i, l, r) fore(i, l, (r) + 1)

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

const int INF = (int)1e9;
const ld EPS = 1e-9;
const ld PI = 3.1415926535897932384626433832795;

int readInt(int l, int r){
  int x;
  if(scanf("%d", &x) != 1){
    fprintf(stderr, "Expected int in range [%d, %d], but haven't found!", l, r);
    throw;

  }
  if(!(l <= x && x <= r)){
    fprintf(stderr, "Expected int in range [%d, %d], but found %d!", l, r, x);
    throw;

  }
  return x;

}

int main(){
  int T = readInt(1, 10);
  forn(Ti, T){
    int n = readInt(1, 100000);
    vector<int> a(n);
    forn(i, n)
      a[i] = readInt(1, 20000);
    vector<li> x(n);
    forn(i, n){
      x[i] = (i == 0 ? 0 : x[i - 1]) + a[i];
    }
    li sum = 0;
    int cnt = 0;
    for(int i = n - 1; i >= 0; --i){
      li left = (i == 0 ? 0 : x[i - 1]);
      if(left == sum)
        cnt++;
      sum += a[i];
    }
    puts(cnt == 0 ? "NO" : "YES");
  }

  return 0;
}
