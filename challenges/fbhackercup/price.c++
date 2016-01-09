#include <cstdio>
#include <algorithm>

typedef unsigned long long ull;

int T;
int N, P;
ull b[100005];
ull pre[100005];

int main () {
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        scanf("%d %d", &N, &P);
        for (int i = 1; i <= N; ++i) {
            scanf("%lld", &b[i]);
            pre[i] = b[i] + pre[i-1];
        }
        ull result = 0;
        for (int i = 0; i <= N; ++i) {
            ull* spot = std::upper_bound(pre + i, pre + N + 1, P + pre[i]);
            if (spot != (pre + i + 1))
                result += spot - (pre + i + 1);
        }
        printf("Case #%d: %lld\n", t, result);
    }
    return 0;
}
