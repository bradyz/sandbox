#include <iostream>
#include <string>
#include <ctype.h>
#include <algorithm>
#include <vector>
#include <queue>
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

bool b[10][10];
bool v[10][10];

string tmp;

bool can (int x, int y) {
    return x >= 0 && x < m && y >= 0 && y < n;
}

void flood (int i, int j, int c, vector<pair<int, int> > &lava) {
    if (!can(i, j) || g[i][j] > c)
        return;
    // cout << "flood: (" << i << ", " << j << ") level: " << g[i][j] << " lava: " << c << endl;
    v[i][j] = false;
    for (int di = 0; di < 8; ++di) {
        int x = i+dr[di];
        int y = j+dc[di];
        if (can(x, y) && v[x][y] && g[x][y] <= c) {
            lava.push_back(pair<int, int>(x, y));
            flood(x, y, c, lava);
        }
    }
}

bool bfs() {
    queue<pair<int, int> >q;
    vector<pair<int, int> > lava;
    int i, j;
    int c = 0;
    int s = 0;
    q.push(pair<int, int>(sx, sy));
    while (q.size() > 0) {
        if (s % 3 != 2) {
            int qs = q.size();
            for (int ti = 0; ti < qs; ++ti) {
                i = q.front().first;
                j = q.front().second;
                q.pop();
                if (g[i][j] == h)
                    return true;
                else if (!v[i][j])
                    continue;
                // cout << "(" << i << ", " << j << ") lava: " << c << " step: " << s << " height: " << g[i][j] << endl;
                for (int di = 0; di < 8; ++di) {
                    int x = i+dr[di];
                    int y = j+dc[di];
                    if (can(x, y) && g[i][j]+1 >= g[x][y] && v[x][y] && !b[x][y]) {
                        b[x][y] = true;
                        q.push(pair<int, int>(x, y));
                    }
                }
            }
        }
        else {
            if (s != 2)
                c += 1;
            else {
                lava.push_back(pair<int, int>(sx, sy));
            }
            // cout << "new: " << c << endl;
            for (int li = 0; li < lava.size(); ++li) {
                flood(lava[li].first, lava[li].second, c, lava);
            }
        } 
        s += 1;
    }
    return false;
}

bool solve () {
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            b[i][j] = false;
            v[i][j] = true;
        }
    }
    return bfs();
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
