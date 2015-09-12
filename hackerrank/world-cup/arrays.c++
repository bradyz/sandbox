#include <iostream>

using namespace std;

const int N = 1e6 + 1;
int n;
int t[2 * N];
int s[2 * N];

void buildT () {
    for (int i = n - 1; i > 0; --i) t[i] = t[i<<1] + t[i<<1|1];
}

void buildS () {
    for (int i = n - 1; i > 0; --i) s[i] = s[i<<1] + s[i<<1|1];
}

void modifyT (int p, int value) {
    for (t[p += n] = value; p > 1; p >>= 1) t[p>>1] = t[p] + t[p^1];
}

void modifyS (int p, int value) {
    for (s[p += n] = value; p > 1; p >>= 1) s[p>>1] = s[p] + s[p^1];
}

int query (int l, int r) {
    int res = 0;
    for (l += n, r += n; l < r; l >>= 1, r >>= 1) {
        if (l&1) {
            res += t[l] * s[l];
            ++l;
        }
        if (r&1) {
            int rp = --r;
            res += t[rp] * s[rp];
        }
    }
    return res;
}

int main() {
    int a;
    int w, x, y, z;

    cin >> n >> a;

    for (int i = 0; i < a; ++i) {
        cin >> w;
        if (w == 3) {
            cin >> y >> z;
            cout << query(y, z+1) << endl;
        }
        else {
            cin >> x >> y >> z;
            for (int j = x; j <= y; ++j)
                if (w == 1)
                    modifyT(j, z);
                else
                    modifyS(j, z);
        }
    }

    return 0;
}
