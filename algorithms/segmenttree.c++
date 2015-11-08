#include <cstdio>
#include <algorithm>

using namespace std;

int n,a,b,t[300000],m,choice;

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

void buildProduct () {
    for(int i = n - 1; i > 0 ; --i) t[i] = t[i<<1] * t[i<<1|1];
}

void modifyProduct (int p, int v) {
    for(t[p += n] = v; p > 1 ; p>>=1) t[p>>1] = t[p] * t[p^1];
}

int queryProduct(int l, int r) {  // sum on interval [l, r)
    int res = 1;
    for (l += n, r += n; l < r; l >>= 1, r >>= 1) {
        if (l&1) res *= t[l++];
        if (r&1) res *= t[--r];
    }
    return res;
}

int main () {
    scanf("%d%d", &n, &m);
    for (int i = 0; i < n; i++) scanf("%d", t + n + i);

    buildProduct();

    for (int i = 0; i < m; i++) {
        scanf("%d%d%d", &choice, &a, &b);
        if (choice == 0) printf("%d\n", queryProduct(a-1,b));
        else modifySum(a - 1, b);
    }
    return 0;
}
