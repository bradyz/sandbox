#include <iostream>
#include <map>
#include <climits>
#include <vector>

using namespace std;

int N, M;
int D, U, C, L;
vector<int> neighbors[10001];
vector<long long> cost[10001];
long long dist[10001];

long long dijkstra () {
    multimap<long long, int> pqueue;
    for (int i = 1; i <= N; ++i)
        dist[i] = INT_MAX;
    dist[1] = 0;
    pqueue.insert(multimap<long long, int>::value_type(0, 1));
    while (!pqueue.empty()) {
        int u = pqueue.begin()->second;
        long long d = pqueue.begin()->first;
        pqueue.erase(pqueue.begin());
        for(int i = 0; i < neighbors[u].size(); i++) {
            long long tmp = d + cost[u][i];
            int v = neighbors[u][i];
            if(tmp < dist[v]) {
                dist[v] = tmp;
                pqueue.insert(multimap<long long, int>::value_type(tmp, v));
            }
        }
    }
    return dist[N];
}

int main () {
    int T;
    cin >> T;
    while (T--) {
       cin >> N >> D >> U >> C >> L;
       for (int i = 1; i <= N; ++i) {
           neighbors[i].clear();
           cost[i].clear();
       }
       for (int i = 1; i <= N; ++i) {
           if (i != N) {
               neighbors[i].push_back(i+1); 
               cost[i].push_back(D); 
           }
           if (i != 1) {
               neighbors[i].push_back(i-1); 
               cost[i].push_back(U); 
           }
       }
       for (int i = 0; i < C; ++i) {
           int u, v, w;
           cin >> u >> v >> w;       
           neighbors[u].push_back(v);
           cost[u].push_back(w);
       }
       for (int i = 0; i < L; ++i) {
           int u, v, w;
           cin >> u >> v >> w;       
           neighbors[u].push_back(v);
           cost[u].push_back(w);
       }
       cout << dijkstra() << endl;
    }
    return 0;
}
