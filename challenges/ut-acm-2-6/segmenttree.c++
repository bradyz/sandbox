#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

#define MAX_N 1000005

int T;
int k, n;
int t[2 * MAX_N];

void buildSum () {
    for (int i = n; i > 0; --i)
        t[i] = min(t[i<<1], t[i<<1|1]);
}

int querySum (int l, int r) {
    int ans = MAX_N;
    for (l+=n, r+=n; l < r; l>>=1, r>>=1)
        ans = min(((l&1) ? t[l++]: MAX_N), ((r&1) ? t[--r]: MAX_N));
    return ans;
}

int main () {
    cin >> T;

    while (T--) {
        cin >> k >> n;
        memset(t, -1, sizeof t);

        for (int i = 1; i <= n; i++)
            cin >> t[n + i];

        buildSum();
        //
        for (int i = 1; i+k <= n+k; i++) {
            cout << querySum(i, i+k) << endl;
        }

        // for(int i = 0; i < n; ++i)
        //     cout << querySum(i, i+1) << endl;
        
        cout << endl;

        cout << 123 << endl;
    }

    return 0;
}
