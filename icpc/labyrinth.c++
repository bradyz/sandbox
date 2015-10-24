#include <iostream>
#include <vector>
#include <unordered_map>

#define INTMAX 2147483646

using namespace std;

struct Point {
    int x, y, weight;
    Point (int a=-1, int b=-1, int c=-1) : x(a), y(b), weight(c) {}
};

int W, H;
int G;
int E;

bool graves[31][31];
Point portals[31][31];
int dist[31][31];

int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};

vector<Point> neighbors (int x, int y) {
    vector<Point> result;
    for (int i = 0; i < sizeof(dx)/sizeof(int); ++i) {
        int xP = x+dx[i];
        int yP = y+dy[i];
        if (xP < 0 || xP >= W || yP < 0 || yP >= H || graves[xP][yP])
            continue;
        if (portals[xP][yP].x != -1) {
            Point tmp = portals[xP][yP];
            result.push_back(Point(tmp.x, tmp.y, tmp.weight+1));
        }
        else {
            result.push_back(Point(xP, yP, 1));
        }
    }
    return result;
}

int main () {
    int x, y;
    int x1, y1, x2, y2, t;
    while (true) {
        cin >>  W >> H;
        if (W == 0 && H == 0)
            break;
        cin >> G;
        for (int i = 0; i < W; ++i) {
            for (int j = 0; j < H; ++j) {
                graves[i][j] = false;
                portals[i][j] = Point();
                dist[i][j] = INTMAX;
            }
        }
        for (int i = 0; i < G; ++i) {
            cin >> x >> y;    
            graves[x][y] = true;
        }
        cin >> E;
        for (int i = 0; i < E; ++i) {
            cin >> x1 >> y1 >> x2 >> y2 >> t;
            portals[x1][y1] = Point(x2, y2, t);
        }
        dist[0][0] = 0;
        bool cycle = false;
        for (int i = 0; i < W * H; ++i) {
            for (int x = 0; x < W; ++x) {
                for (int y = 0; y < H; ++y) {
                    for (auto it: neighbors(x, y)) {
                        if (dist[it.x][it.y] > dist[x][y] + it.weight) {
                            if (i == W * H - 1)
                                cycle = true;
                            dist[it.x][it.y] = dist[x][y] + it.weight;
                        }                        
                    }
                }
            }
        }
        if (cycle)
            cout << "NEVER" << endl;
        else if (dist[W-1][H-1] == INTMAX)
            cout << "IMPOSSIBLE" << endl;
        else
            cout << dist[W-1][H-1] << endl;
    }
    return 0;
}
