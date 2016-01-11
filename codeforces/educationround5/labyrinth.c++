#include <iostream>
#include <utility>
#include <vector>
#include <algorithm>

using namespace std;

typedef pair<int, int> ii;

int DX[] = {-1, 1, 0, 0};
int DY[] = {0, 0, -1, 1};

int N, M;
ii par[1005][1005];
char grid[1005][1005];
int size[1005][1005];
bool vis[1005][1005];

void dfs (int i, int j) {
    vis[i][j] = true;
    vector<ii> result;
    vector<ii> the_stack;
    the_stack.push_back(ii(i, j));
    while (the_stack.size() > 0) {
        int x = the_stack.back().first; 
        int y = the_stack.back().second;
        the_stack.pop_back();
        result.push_back(ii(x, y));
        for (int i = 0; i < 4; ++i) {
            int xp = x + DX[i];
            int yp = y + DY[i];
            if (xp < 0 || xp >= N || yp < 0 || yp >= M)
                continue;
            else if (grid[xp][yp] == '*' || vis[xp][yp])
                continue;
            vis[xp][yp] = true;
            the_stack.push_back(ii(xp, yp));
        }
    }
    for (auto it: result) {
        par[it.first][it.second] = ii(i, j);
        size[it.first][it.second] = result.size();
    }
}

int main () {
    cin >> N >> M;
    for (int i = 0; i < N; ++i)
        cin >> grid[i];
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            if (vis[i][j])
                continue;
            else if (grid[i][j] == '*')
                continue;
            dfs(i, j);
        }
    }
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            if (grid[i][j] == '*') {
                int tmp = 1;
                vector<ii> seen;
                for (int x = 0; x < 4; ++x) {
                    int xp = i + DX[x];
                    int yp = j + DY[x];
                    if (xp < 0 || xp >= N || yp < 0 || yp >= M)
                        continue;
                    else if (grid[xp][yp] == '*')
                        continue;
                    else if (find(seen.begin(), seen.end() , par[xp][yp]) != seen.end())
                        continue;
                    seen.push_back(par[xp][yp]);
                    tmp += size[xp][yp];
                }
                cout << tmp % 10;
            }
            else
                cout << '.';
        }
        cout << endl;
    }
    return 0;
}
