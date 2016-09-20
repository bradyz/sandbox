#include <iostream>
#include <map>
#include <climits>
#include <unordered_map>
#include <vector>

using namespace std;

int N, M;
vector<int> neighbors[10001];
vector<long long> cost[10001];
unordered_map<int, int> parent;
long long dist[10001];

void dijkstra () {
    multimap<long long, int> pqueue;
    for (int i = 1; i <= N; ++i)
        dist[i] = INT_MAX;
    dist[1] = 0;
    parent[1] = -1;
    pqueue.insert(multimap<long long, int>::value_type(0, 1));
    while (!pqueue.empty()) {
        int u = pqueue.begin()->second;
        long long d = pqueue.begin()->first;
        pqueue.erase(pqueue.begin());
        for(int i = 0; i < neighbors[u].size(); i++) {
            long long tmp = d + cost[u][i];
            int v = neighbors[u][i];
            if(tmp < dist[v]) {
                parent[v] = u;
                dist[v] = tmp;
                pqueue.insert(multimap<long long, int>::value_type(tmp, v));
            }
        }
    }
}
