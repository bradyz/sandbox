#include <iostream>

using namespace std;

long long n, k;
long long a[100005];
long long b[100005];

bool can(long long x) {
  long long kt = k;
  for (long long i = 0; i < n; ++i) {
    if (b[i] + kt < a[i] * x)
      return false;
    kt -= max(0ll, a[i] * x - b[i]);
  }
  return true;
}

int main () {
  cin >> n >> k;
  for (long long i = 0; i < n; ++i)
    cin >> a[i];
  for (long long i = 0; i < n; ++i)
    cin >> b[i];
  long long lo = 0;
  long long hi = 2000000005;
  long long mi;
  while (lo <= hi) {
    mi = (lo + hi) / 2;
    if (can(mi)) 
      lo = mi + 1;
    else
      hi = mi - 1;
  }
  cout << (lo+hi)/2 << endl;
  return 0;
}
