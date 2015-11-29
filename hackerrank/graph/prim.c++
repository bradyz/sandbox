#include <iostream>
#include <algorithm>
#include <utility>
#include <vector>
#include <unordered_set>
#include <map>

using namespace std;

typedef pair<int, int> ii;
typedef vector<ii> vii;

int N, M;
int S;
unordered_set<int> vis;
vii graph[3010];

long long prim () {
    multimap<int, int> pqueue;
    long long total = 0;
    for (int u = 1; u <= N; ++u)
        vis.insert(u);
    pqueue.insert(multimap<int, int>::value_type(0, S));
    while (vis.size() > 0) {
        int u = pqueue.begin()->second;
        int cost = pqueue.begin()->first;
        pqueue.erase(pqueue.begin());
        if (vis.find(u) != vis.end()) {
            // cout << "got: " << u << " cost: " << cost << endl;
            vis.erase(u);
            total += cost;
        }
        for (ii v: graph[u]) {
            if (vis.find(v.first) == vis.end())
                continue;
            pqueue.insert(multimap<int, int>::value_type(v.second, v.first));
        }
    }
    return total;
}

int main () {
    cin >> N >> M;
    for (int m = 0; m < M; ++m) {
        int u, v, w;
        cin >> u >> v >> w;
        graph[u].push_back(ii(v, w));
        graph[v].push_back(ii(u, w));
    }
    cin >> S;
    cout << prim() << endl;
    return 0;
}
