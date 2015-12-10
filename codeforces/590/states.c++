#include <iostream>
#include <queue>
#include <utility>

using namespace std;

struct point {
    int x, y;
    point (int a=-1, int b=-1) : x(a), y(b) {}
};

const int DX[] = {-1, 1, 0, 0};
const int DY[] = {0, 0, -1, 1};

int N, M;
char grid[1001][1001];
int dist[1001][1001][1001][1001];
point par[1001][1001];

void build () {
    for (int x = 0; x < N; ++x) {
        for (int y = 0; y < M; ++y) {
            for (int d = 0; d < 4; ++d) {
                int xp = x+DX[d];
                int yp = y+DY[d];
                if (grid[x][y] == '#' || grid[x][y] == '#')
                    continue;
                else if (grid[x][y] == '.' || grid[x][y] == '.')
                    dist[x][y][xp][yp] = 1;
                else
                    dist[x][y][xp][yp] = 0;
            }
        }
    }
}

int main () {
    string row;
    point s1;
    point s2;
    point s3;
    cin >> N >> M;
    for (int i = 0; i < N; ++i) {
        cin >> row;
        for (int j = 0; j < M; ++j) {
            grid[i][j] = row[j];
            if (grid[i][j] == '1')
                s1 = point(i, j);
            else if (grid[i][j] == '2')
                s2 = point(i, j);
            else if (grid[i][j] == '3')
                s3 = point(i, j);
        }
    }
    return 0;
}
