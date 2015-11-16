#include <iostream>
#include <string>
#include <vector>

using namespace std;

int dx[] = {0, 0, 1, -1};
int dy[] = {1, -1, 0, 0};

int N, M, K;

bool vis[1001][1001];
char grid[1001][1001];
int paintings[1001][1001];

struct Point {
    int x, y;
    Point (int a, int b) : x(a), y(b) {}
};

int dfs (int x, int y, vector<Point>& path) {
    int number = 0;
    path.push_back(Point(x, y));
    for (int i = 0; i < 4; ++i) {
        int xp = x + dx[i];
        int yp = y + dy[i];
        if (xp < 0 || xp >= N || yp < 0 || yp >= M || vis[xp][yp])
            continue;
        if (grid[xp][yp] == '*')
            number += 1;  
        else {
            vis[xp][yp] = true;
            number += dfs(xp, yp, path);
        }
    }
    return number;
}

int main () {
    cin >> N >> M >> K;
    for (int n = 0; n < N; ++n) {
        string tmp;
        cin >> tmp;
        for (int m = 0; m < tmp.size(); ++m)
            grid[n][m] = tmp[m];
    }
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            paintings[i][j] = 0;
            vis[i][j] = false;
        }
    }
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            if (grid[i][j] == '.' && !vis[i][j]) {
                vis[i][j] = true;
                vector<Point> path;
                int number = dfs(i, j, path);
                for (auto p: path)
                    paintings[p.x][p.y] = number;
            }
        }
    }
    for (int k = 0; k < K; ++k) {
        int x, y;
        cin >> x >> y;
        cout << paintings[x-1][y-1] << endl;
    }
}
