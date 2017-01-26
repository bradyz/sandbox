#include <iostream>
#include <set>

using namespace std;

int n, t;
int factors[100005];

void f(int x) {
  set<int> c;
  for (int i = 2; i * i <= x; i++) {
    while (x % i == 0) {
      c.insert(i);
      x /= i;
    }
  }
  if (x > 1)
    c.insert(x);
  for (int y : c)
    factors[y]++;
}

int main () {
  for (int i = 0; i < 100005; i++)
    factors[i] = 0;
  cin >> n;
  for (int i = 0; i < n; i++) {
    cin >> t;
    f(t);
  }
  int r = 1;
  for (int i = 0; i < 100005; i++)
    r = max(r, factors[i]);
  cout << r << endl;
  return 0;
}
