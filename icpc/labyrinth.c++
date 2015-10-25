#include <iostream>
#include <vector>

#define INF 1 << 30

using namespace std;

struct Point {
    int x, y, w;
    Point (int a, int b, int c) : x(a), y(b), w(c) {}
};

const int DX[] = {-1, 1, 0, 0};
const int DY[] = {0, 0, -1, 1};

int W, H; 
int G;
int E;

bool graves[31][31];
int dist[31][31];
vector<Point> neighbors[31][31];

// returns true if negative cycle
bool bellmondford () {
    dist[0][0] = 0;
    // longest path through the grid is number of valid vertices - 1
    for (int i = 0; i < W * H - G - 1; ++i) {
        for (int x = 0; x < W; ++x) {
            for (int y = 0; y < H; ++y) {
                if (dist[x][y] >= INF) continue;
                // relax the edge
                for (auto v: neighbors[x][y])
                    dist[v.x][v.y] = min(dist[v.x][v.y], dist[x][y] + v.w);
            }
        }
    }
    // negative cycle detection
    bool cycle = false;
    for (int x = 0; x < W; ++x) {
        for (int y = 0; y < H; ++y) {
            if (dist[x][y] >= INF) continue;
            for (auto v: neighbors[x][y]) {
                // if any distance decreased, we have a negative cycle
                if (dist[v.x][v.y] > dist[x][y] + v.w)
                    return true;
            }
        }
    }
    return false;
}

int main () {
    while (cin >> W >> H && W && H) {
        // clear the grid
        for (int i = 0; i <= W; ++i) {
            for (int j = 0; j <= H; ++j) {
                graves[i][j] = false;
                dist[i][j] = INF;
                neighbors[i][j].clear();
            }
        }
        // marking graves
        cin >> G;
        for (int i = 0; i < G; ++i) {
            int x, y;
            cin >> x >> y;    
            graves[x][y] = true;
        }
        // adding edge for each portal
        cin >> E;
        for (int i = 0; i < E; ++i) {
            int x1, y1, x2, y2, t;
            cin >> x1 >> y1 >> x2 >> y2 >> t;
            neighbors[x1][y1].push_back(Point(x2, y2, t));
        }
        // finding neighbors
        for (int x = 0; x < W; ++x) {
            for (int y = 0; y < H; ++y) {
                // dont relax goal node
                if (x == W-1 && y == H-1) continue;
                // haunted holes only have one neighbor
                if (neighbors[x][y].size() > 0) continue;
                for (int i = 0; i < 4; ++i) {
                    // neighbor node
                    int xP = x+DX[i];
                    int yP = y+DY[i];
                    // continue if not in bounds or there is a grave
                    if (xP < 0 || xP >= W || yP < 0 || yP >= H || graves[xP][yP])
                        continue;
                    neighbors[x][y].push_back(Point(xP, yP, 1));
                }
            }
        }
        // bellmond ford returns true if negative cycle
        if (bellmondford())
            cout << "Never" << endl;
        else if (dist[W-1][H-1] >= INF)
            cout << "Impossible" << endl;
        else
            cout << dist[W-1][H-1] << endl;
    }
    return 0;
}
