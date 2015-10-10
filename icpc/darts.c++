#include <iostream>
#include <cmath>

using namespace std;

int v[] = {20, 40, 60, 80, 100, 120, 140, 160, 180, 200};

int t, ct;
int n;
int x, y;

int main () {
    cin >> t;

    for (ct = 0; ct < t; ++ct) {
        cin >> n;
        int r = 0;
        for (int i = 0; i < n; ++i) {
            cin >> x >> y;
            int s = (x * x) + (y * y);
            for (int j = 0; j < sizeof(v) / sizeof(int); ++j) {
                if (s <= v[j]*v[j]) {
                    r += 10-j;
                    // cout << s << " " << 10-j << endl;
                    break;
                }
            }

        }
        cout << r << endl;
    }

}
