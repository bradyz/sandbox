#include <iostream>
#include <queue>
#include <utility>

using namespace std;

bool g[5001][5001];
bool v[5001];
int n, m;
int x, y;
int q, k;
int t;

bool dfs (int c, int s) {
    if (v[c] || v[q] || s > k)
        return false;
    else if (c == q && s <= k && (k-s) % 2 == 0)
        return true;

    v[c] = true;
    
    bool r = false;

    for (int i = 1; i < n+1; ++i) {
        if (g[c][i])
            r |= dfs(i, s+1);
    }

    v[c] = false;

    return r;
}

bool bfs (int e) {
    bool r;
    queue<pair<int, int> > q;

    q.push(pair<int, int> (1, 0));

    while (q.size() > 0 && !r) {
        int a = q.front().first;
        int b = q.front().second;

        q.pop();
        
        if (b > k)
            continue;
        else if (a == e && b <= k && k-b % 2 == 0) {
            return true;
            continue;
        }

        v[a] = true;

        for (int i = 1; i < n+1; ++i) {
            if (g[a][i] && !v[i])
                q.push(pair<int, int> (i, b+1));
        }
    }

    return false;
}

int main () {
    ios::sync_with_stdio(false);

    cin >> n >> m;

    for (int i = 0; i < m; ++i) {
        cin >> x >> y;
        g[x][y] = true;
        g[y][x] = true;
    }

    cin >> t;

    for (int i = 0; i < t; ++i) {
        cin >> q >> k;
        cout << bfs(q) << endl;
    }
}
