#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

int T;
int n, m;
long long t[150000 * 2 + 5];

void buildSum () {
    for(int i = n - 1; i > 0 ; --i) t[i] = (t[i<<1] + t[i<<1|1]);
}

void modifySum (int p, int v) {
    for(t[p += n] = v; p > 1 ; p>>=1) t[p>>1] = (t[p] + t[p^1]);
}

int querySum (int l, int r) {
    int ans = 0;
    for(l+=n, r+=n; l < r; l>>=1, r>>=1)
        ans += ((l&1) ? t[l++] : 0) + ((r&1) ? t[--r] : 0 );
    return ans;
}

int main () {
    cin >> T;
    while (T--) {
        cin >> n >> m;
        memset(t, 0, 4 * n);
        for (int i = 0; i < n; ++i) {
            int tmp;
            cin >> t[n + i];
        }
        buildSum();
        long long buh = 0;
        for (int i = 0; i < m; ++i) {
            string tmp;
            int x, y;
            // for (int i = 0; i < n; ++i)
            //     cout << "i: " << i << " val: " << querySum(i, i+1) << endl;
            // cout << "buh: " << buh << endl;
            cin >> tmp;
            if (tmp == "ADD") {
                cin >> x >> y;
                long long pre = querySum(x, x+1);
                buh -= y;
                modifySum(x, pre + y);
            }
            else if (tmp == "MULTIPLY") {
                cin >> x >> y;
                long long pre = querySum(x, x+1);
                modifySum(x, pre * y);
                buh -= t[n+x] - pre;
            }
            else if (tmp == "GET") {
                cin >> x >> y;
                cout << querySum(x, y+1) << endl;
            }
            else 
                cout << buh << endl;
        }
    }

    return 0;
}
