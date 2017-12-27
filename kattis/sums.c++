#include <iostream>

using namespace std;

typedef long long ll;

ll t, x;

void solve(){
    for (ll n = 1; n * (n + 1) / 2 < x; n++) {
        ll a = (x - (n * (n + 1)) / 2) / (n + 1);
        ll r = (n + 1) * a + (n * (n + 1)) / 2;

        if (r == x) {
          cout << x << " = ";
          for (int i = a; i < a + n; i++)
            cout << i << " + ";
          cout << a + n << endl;
          return;
        }
    }

    cout << "IMPOSSIBLE" << endl;
}

int main() {
  cin >> t;

  for (int i = 0; i < t; i++) {
    cin >> x;

    solve();
  }

  return 0;
}
