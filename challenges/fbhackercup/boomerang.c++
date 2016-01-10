#include <cstdio>
#include <unordered_map>
#include <utility>

using namespace std;

typedef pair<int, int> ii;

int T;
int N;
unordered_map<int, int> dist[2005];
ii points[2005];

int factorial (int n) {
    return (n == 1) ? 1: factorial(n - 1) * n;
}

int choose_two (int n) {
    return factorial(n) / factorial(n-2) / factorial(2);
}

int main () {
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        scanf("%d", &N);
        for (int n = 0; n < N; ++n) {
            dist[n].clear();
            int u, v;
            scanf("%d %d", &u, &v);
            points[n] = ii(u, v);
        }
        for (int i = 0; i < N; ++i) {
            for (int j = i + 1; j < N; ++j) {
                int dx = (points[i].first - points[j].first);
                int dy = (points[i].second - points[j].second);
                int d = dx * dx + dy * dy;
                if (dist[i].find(d) != dist[i].end())
                    ++dist[i][d];
                else
                    dist[i][d] = 1;
                if (dist[j].find(d) != dist[j].end())
                    ++dist[j][d];
                else
                    dist[j][d] = 1;
            }
        }
        int result = 0;
        for (int i = 0; i < N; ++i) {
            for (auto it: dist[i]) {
                if (it.second < 2)
                    continue;
                result += choose_two(it.second);
            }
        }
        printf("Case #%d: %d\n", t, result);
    }
    return 0;
}
