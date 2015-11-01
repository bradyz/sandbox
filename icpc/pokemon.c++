#include <iostream>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <vector>

using namespace std;

struct Point {
    int v;
    double p;
    Point (int a, double b) : v(a), p(b) {}
};

int T;
int V, E;
double prob[1001];
vector<Point> cost[1001];

int main () {
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cin >> V >> E;
        memset(prob, 0, sizeof(prob));
        for (int i = 0; i < V; ++i)
            cost[i].clear();
        for (int e = 0; e < E; ++e) {
            int u, v;
            double p;
            cin >> u >> v >> p;
            cost[u].push_back(Point(v, p));
            cost[v].push_back(Point(u, p));
        }
        prob[0] = 1;
        for (int k = 0; k < V-1; ++k) {
            for (int u = 0; u < V; ++u) {
                if (prob[u] == 0)
                    continue;
                for (auto v: cost[u]) {
                    prob[v.v] = max(prob[v.v], prob[u]*v.p);
                }
            }
        }
        cout << "Case " << t << ": " << round(prob[1] * 100) / 100.0  << endl;
    }
    return 0;
}
