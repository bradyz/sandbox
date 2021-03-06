#include <iostream>
#include <map>
#include <climits>
#include <unordered_map>
#include <vector>

using namespace std;

typedef long long weight;

int T;
int N, M;
int S;
vector<int> neighbors[10001];
vector<weight> cost[10001];
unordered_map<int, int> parent;
weight dist[10001];

void dijkstra () {
    multimap<weight, int> pqueue;
    for (int i = 1; i <= N; ++i)
        dist[i] = INT_MAX;
    dist[S] = 0;
    parent[S] = -1;
    pqueue.insert(multimap<weight, int>::value_type(0, S));
    while (!pqueue.empty()) {
        int u = pqueue.begin()->second;
        weight d = pqueue.begin()->first;
        pqueue.erase(pqueue.begin());
        for(int i = 0; i < neighbors[u].size(); i++) {
            weight tmp = d + cost[u][i];
            int v = neighbors[u][i];
            if(tmp < dist[v]) {
                parent[v] = u;
                dist[v] = tmp;
                pqueue.insert(multimap<weight, int>::value_type(tmp, v));
            }
        }
    }
}

int main () {
    cin >> T;
    while (T--) {
        cin >> N >> M;
        parent.clear();
        for (int u = 1; u <= N; ++u) {
            neighbors[u].clear();
            cost[u].clear();
        }
        for (int m = 0; m < M; ++m) {
            int u, v, w;
            cin >> u >> v >> w;
            neighbors[u].push_back(v);
            neighbors[v].push_back(u);
            cost[u].push_back(w);
            cost[v].push_back(w);
        }
        cin >> S;
        dijkstra();
        for (int u = 1; u <= N; ++u) {
            if (u == S)
                continue;
            if (dist[u] == INT_MAX)
                cout << -1 << " ";
            else
                cout << dist[u] << " ";
        }
        cout << endl;
    }
}
