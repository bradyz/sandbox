#include <iostream>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <vector>
#include <map>

using namespace std;

typedef double weight;

int T;
int V, E;

int n;
vector<int> neighbors[1001];
vector<weight> cost[1001];
weight dist[1001];
multimap<weight, int> pqueue;

double dijkstra () {
    dist[0] = 1;
    pqueue.clear();
    pqueue.insert(multimap<weight, int>::value_type(1, 0));
    while (!pqueue.empty()) {
        int u = pqueue.rbegin()->second;
        weight d = pqueue.rbegin()->first;
        pqueue.erase(--pqueue.rbegin().base());
        for(int i = 0; i < neighbors[u].size(); i++) {
            weight tmp = d * cost[u][i];
            int v = neighbors[u][i];
            if(dist[v] < 0 || tmp > dist[v]) {
                dist[v] = tmp;
                pqueue.insert(multimap<weight, int>::value_type(tmp, v));
            }
        }
    }
    return dist[1];
}

int main () {
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cin >> V >> E;
        for (int i = 0; i < V; ++i) {
            neighbors[i].clear();
            cost[i].clear();
            dist[i] = -1;
        }
        for (int i = 0; i < E; ++i) {
            int u, v;
            double p;
            cin >> u >> v >> p;
            neighbors[u].push_back(v);
            cost[u].push_back(p);
            neighbors[v].push_back(u);
            cost[v].push_back(p);
        }
        printf("Case %d: %.2f\n", t, dijkstra());
    }
    return 0;
}
