#include <iostream>

using namespace std;

int a[45000000];
int n;
int t;
int g;

int main () {
    cin >> t;
    while (t--) {
        cin >> n;
        int c = 0;
        for (int i = 0; i < n; ++i) {
            int x;
            cin >> x;
            for (int j = c; j <= c + x; ++j)
                a[j] = x;
            c += x;
            // for (int i = 0; i < c; ++i)
            //     cout << a[i] << " ";
            // cout << endl;
        }
        cin >> g;
        int ret = 0;
        for (int i = 0; i < g; ++i) {
            int q;
            cin >> q;
            ret = max(ret, a[q]);
        }
        cout << ret << endl;
    }
    return 0;
}
