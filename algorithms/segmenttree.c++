#include <iostream>
#include <algorithm>

using namespace std;

int n, m;
int a, b;
int t[300000];
int choice;

void buildSum () {
    for (int i = n - 1; i > 0 ; --i) 
        t[i] = (t[i<<1] + t[i<<1|1]);
}

void modifySum (int p, int v) {
    for (t[p += n] = v; p > 1 ; p>>=1)
        t[p>>1] = (t[p] + t[p^1]);
}

int querySum (int l, int r) {
    int ans = 0;
    for (l+=n, r+=n; l < r; l>>=1, r>>=1)
        ans += ((l&1) ? t[l++] : 0) + ((r&1) ? t[--r] : 0 );
    return ans;
}

void buildProduct () {
    for (int i = n - 1; i > 0 ; --i)
        t[i] = t[i<<1] * t[i<<1|1];
}

void modifyProduct (int p, int v) {
    for (t[p += n] = v; p > 1 ; p>>=1)
        t[p>>1] = t[p] * t[p^1];
}

// sum on interval [l, r)
int queryProduct(int l, int r) {
    int res = 1;
    for (l += n, r += n; l < r; l >>= 1, r >>= 1) {
        if (l&1) res *= t[l++];
        if (r&1) res *= t[--r];
    }
    return res;
}

int gcd (int a, int b) {
    if (b == 0)
        return a;
    return gcd(b, a % b);
}

void buildGcd () {
    for (int i = n - 1; i > 0 ; --i) 
        t[i] = gcd(t[i<<1], t[i<<1|1]);
}

void modifyGcd (int p, int v) {
    for (t[p += n] = v; p > 1 ; p>>=1)
        t[p>>1] = gcd(t[p], t[p^1]);
}

int queryGcd (int l, int r) {
    int ans = 0;
    for (l+=n, r+=n; l < r; l>>=1, r>>=1) {
        if (l & 1)
            ans = gcd(t[l++], ans);
        if (r & 1)
            ans = gcd(t[--r], ans);
    }
    return ans;
}

int main () {
    cin >> n >> m;

    for (int i = 0; i < n; i++)
        cin >> t[n+i];

    buildGcd();

    // for (int i = 0; i < m; i++) {
    //     cin >> choice >> a >> b;
    //     if (choice == 0)
    //         cout << queryGcd(a-1, b) << endl;
    //     else
    //         modifySum(a - 1, b);
    // }

    for (int i = 1; i <= n; ++i) {
        for (int j = i; j <= n; ++j) {
            for (int k = i; k <= j; ++k)
                cout << queryGcd(k-1, k) << " ";
            cout << endl;
            cout << queryGcd(i-1, j) << endl;
        }
    }
    return 0;
}
