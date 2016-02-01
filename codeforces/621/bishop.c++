#include <iostream>

using namespace std;

#define MAX_N 1005

int N;
bool grid[MAX_N][MAX_N];
bool vis1[MAX_N][MAX_N];
bool vis2[MAX_N][MAX_N];

long long choose(long long n, long long k) {
    if (k > n)
        return 0;
    long long r = 1;
    for (long long d = 1; d <= k; ++d) {
        r *= n--;
        r /= d;
    }
    return r;
}

int main () {
    cin >> N;
    for (int i = 0; i < N; ++i) {
        int x, y;
        cin >> x >> y;
        grid[x-1][y-1] = true;
    }
    long long ret = 0;
    for (int i = 0; i < MAX_N; ++i) {
        for (int j = 0; j < MAX_N; ++j) {
            long long tmp1 = 0, tmp2 = 0;
            for (int dx = 0, dy = 0;; ++dx, ++dy) {
                if (i+dx < 0 || i+dx >= MAX_N-1 || j+dy < 0 || j+dy >= MAX_N-1)
                    break;
                else if (vis1[i+dx][j+dy])
                    break;
                vis1[i+dx][j+dy] = true;
                tmp1 += grid[i+dx][j+dy];
            }
            for (int dx = 0, dy = 0;; ++dx, --dy) {
                if (i+dx < 0 || i+dx >= MAX_N-1 || j+dy < 0 || j+dy >= MAX_N-1)
                    break;
                else if (vis2[i+dx][j+dy])
                    break;
                vis2[i+dx][j+dy] = true;
                tmp2 += grid[i+dx][j+dy];
            }
            ret += choose(tmp1, 2) + choose(tmp2, 2);
        }
    }
    cout << ret << endl;
    return 0;
}
