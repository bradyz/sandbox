#include <cstdio>
#include <utility>
#include <queue>

using namespace std;

typedef pair<int, bool*> pibp;

int n, q;
queue<pibp> c[300005];
queue<pibp> e;

int main () {
    scanf("%d %d", &n, &q);
    long long r = 0;
    long long t = 0;
    for (int i = 0; i < q; ++i) {
        int z, x;
        scanf("%d %d", &z, &x);
        if (z == 1) {
            bool *p = new bool();
            *p = false;
            e.push(pibp(t, p));
            c[x].push(pibp(t, p));
            pibp tmp(t, p);
            ++t;
        }
        else if (z == 2) {
            while (c[x].empty() == false) {
                if (*(c[x].front().second) == false)
                    ++r;
                *(c[x].front().second) = true;
                c[x].pop();
            }
        }
        else {
            while (e.size() > 0 && e.front().first < x) {
                if (*e.front().second == false)
                    ++r;
                *e.front().second = true; 
                e.pop();
            }
        }
        printf("%d\n", t - r);
    }
    return 0;
}
