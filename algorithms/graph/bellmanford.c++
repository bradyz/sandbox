#include <iostream>
#include <vector>

#define INF 1 << 30

using namespace std;

struct Point {
    // x, y, weight
    int x, y, w;
    Point (int a, int b, int c) : x(a), y(b), w(c) {}
};

int W, H; 

// distance from source
long long dist[31][31];
// neighbors of point x, y
vector<Point> neighbors[31][31];

// returns true if negative cycle
bool bellmanford () {
    // initialize all to be unreachable
    for (int x = 0; x < W; x++)
        for (int y = 0; y < H; y++)
            dist[x][y] = INF;
    // the source is 0, 0
    dist[0][0] = 0;
    // iterate number of vertices - 1 times
    for (int i = 0; i < W * H - 1; ++i) {
        // pick an x
        for (int x = 0; x < W; ++x) {
            // pick a y
            for (int y = 0; y < H; ++y) {
                // cant reach this point (yet?)
                if (dist[x][y] >= INF) continue;
                // iterate through neighbors, relax the edge
                for (Point v: neighbors[x][y])
                    dist[v.x][v.y] = min(dist[v.x][v.y], dist[x][y] + v.w);
            }
        }
    }
    // negative cycle detection
    bool cycle = false;
    // pick an x
    for (int x = 0; x < W; ++x) {
        // pick a y
        for (int y = 0; y < H; ++y) {
            if (dist[x][y] >= INF) continue;
            // iterate through edges
            for (Point v: neighbors[x][y]) {
                // if any distance decreased, we have a negative cycle
                if (dist[v.x][v.y] > dist[x][y] + v.w)
                    return true;
            }
        }
    }
    return false;
}

