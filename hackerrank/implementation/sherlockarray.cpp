#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

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

  // forn(Ti, T){
  for(int Ti = 0; Ti < T; Ti++) {
    int n = readInt(1, 100000);
    vector<int> a(n);

    // forn(i, n)
    for(int i = 0; i < n; i++)
      a[i] = readInt(1, 20000);

    vector<long long> x(n);

    // forn(i, n){
    for(int i = 0; i < n; i++) {
      x[i] = (i == 0 ? 0 : x[i - 1]) + a[i];
    }

    long long sum = 0;

    int cnt = 0;

    for(int i = n - 1; i >= 0; --i) {
      long long left = (i == 0 ? 0 : x[i - 1]);
      if(left == sum)
        cnt++;
      sum += a[i];
    }

    puts(cnt == 0 ? "NO" : "YES");
  }

  return 0;
}
