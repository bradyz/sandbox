#include <iostream>
#include <map>
#include <climits>
#include <unordered_map>
#include <vector>

using namespace std;

typedef long long weight;

int N, M;
vector<int> neighbors[10001];
vector<weight> cost[10001];
unordered_map<int, int> parent;
weight dist[10001];

void dijkstra () {
    multimap<weight, int> pqueue;
    for (int i = 1; i <= N; ++i)
        dist[i] = INT_MAX;
    dist[1] = 0;
    parent[1] = -1;
    pqueue.insert(multimap<weight, int>::value_type(0, 1));
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
    cin >> N >> M; 
    for (int m = 0; m < M; ++m) {
        int u, v;
        weight w;
        cin >> u >> v >> w;
        neighbors[u].push_back(v);
        cost[u].push_back(w);
    }
    dijkstra();
    vector<int> result;
    int cur = N;
    while (cur != -1) {
        result.push_back(cur);
        cur = parent[cur];
    }
    for (auto it = result.rbegin(); it != result.rend(); ++it)
        cout << *it << " ";
    cout << endl;

    return 0;
}
