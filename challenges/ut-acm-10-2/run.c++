#include <iostream>
#include <string>
#include <ctype.h>
#include <algorithm>
#include <vector>
#include <utility>

using namespace std;

int t, ct;
int m, n;
int g[10][10];

int l, h;
int sx = -1;
int sy = -1;

int dr[] = {-1, -1, -1, 0, 0, 1, 1, 1};
int dc[] = {-1, 0, 1, -1, 1, -1, 0, 1};

int b[10][10];
bool v[10][10];

string tmp;

bool can (int x, int y) {
    return x >= 0 && x < m && y >= 0 && y < n;
}

void flood (int i, int j, int c, vector<pair<int, int> > ln) {
    if (!can(i, j) || !v[i][j] || g[i][j] > c)
        return;
    cout << "flood: (" << i << ", " << j << ") level: " << g[i][j] << " lava: " << c << endl;
    v[i][j] = false;
    ln.push_back(pair<int, int>(i, j));
    for (int di = 0; di < 8; ++di) {
        int x = i+dr[di];
        int y = j+dc[di];
        if (can(x, y) && v[i][j] && g[i][j] <= c) {
            flood(x, y, c, ln);
        }
    }
}

bool dfs(int i, int j, int c, int s) {
    if (g[i][j] == h)
        return true;
    else if (!v[i][j])
        return false;
    if (s % 3 != 2) {
        if (b[i][j] < s) 
            return false;
        b[i][j] = s;
        cout << "(" << i << ", " << j << ") lava: " << c << " step: " << s << " height: " << g[i][j] << endl;
        for (int di = 0; di < 8; ++di) {
            int x = i+dr[di];
            int y = j+dc[di];
            if (can(x, y) && g[i][j]+1 >= g[x][y] && v[x][y]) {
                if (dfs(x, y, c, s+1))
                    return true;
            }
        }
    }
    else {
        if (s == 2)  {
            v[sx][sy] = false;
            if (dfs(i, j, c, s+1))
                return true;
            v[sx][sy] = true;
        }
        else {
            vector<pair<int, int> > ln;
            cout << "sit: " << i << " " << j << endl;
            for (int li = 0; li < 8; ++li) {
                for (int lj = 0; lj < 8; ++lj) {
                    flood(li, lj, c+1, ln);
                }
            }
            if (dfs(i, j, c+1, s+1))
                return true;
            for (int ti = 0; ti < ln.size(); ++ti) 
                v[ln[ti].first][ln[ti].second] = true;
        }
    }
    return false;
}

bool solve () {
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            b[i][j] = 36;
            v[i][j] = true;
        }
    }
    return dfs(sx, sy, 0, 0);
}

int main () {
    cin >> t;

    for (ct = 0; ct < t; ++ct) {
        cin >> m >> n;
        l = 36;
        h = -1;
        for (int i = 0; i < m; ++i) {
            cin >> tmp;
            for (int j = 0; j < n; ++j) {
                if (isdigit(tmp[j]))
                    g[i][j] = tmp[j] - '0';
                else
                    g[i][j] = 10 + (tmp[j] - 'A');
                if (g[i][j] < l) {
                    l = g[i][j];
                    sx = i;
                    sy = j;
                }
                h = max(h, g[i][j]);
            }
        }     
        if (solve())
            cout << "Case " << ct+1 << ": SAFE" << endl;
        else
            cout << "Case " << ct+1 << ": MELTED" << endl;
    }

    return 0;
}
