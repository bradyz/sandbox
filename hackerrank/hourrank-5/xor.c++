#include <iostream>

using namespace std;

const int n = 150000;
int m;
int t[2 * n];

void buildSum () {
    for (int i = n - 1; i > 0; --i)
        t[i] = (t[i<<1] ^ t[i<<1 | 1]);
}

int querySum (int l, int r) {
    int ans = 0;
    for(l += n, r += n; l < r; l >>= 1, r >>= 1)
        ans ^= ((l & 1) ? t[l++] : 0) ^ ((r & 1) ? t[--r]: 0);
    return ans;
}

int main () {
    for (int i = 1; i < n; i++)
        t[n + i] = (i - 1) ^ t[n + i - 1];

    buildSum();

    scanf("%d", &m);
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        cout << querySum(a+1, b+2) << endl;
    }
    return 0;
}
