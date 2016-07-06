#include <iostream>
#include <map>
#include <climits>
#include <unordered_map>
#include <vector>

using namespace std;

int N;
int a[200005];
int dist[200005];

void dijkstra () {
    multimap<int, int> pqueue;
    for (int i = 1; i <= N; ++i)
        dist[i] = INT_MAX;
    dist[1] = 0;
    pqueue.insert(multimap<int, int>::value_type(0, 1));
    while (!pqueue.empty()) {
        int u = pqueue.begin()->second;
        int d = pqueue.begin()->first;
        pqueue.erase(pqueue.begin());

        int v = a[u];
        int tmp = d + 1;
        if(tmp < dist[v]) {
          dist[v] = tmp;
          pqueue.insert(multimap<int, int>::value_type(tmp, v));
        }

        if (u + 1 <= N) {
          int v = u + 1;
          int tmp = d + 1;
          if(tmp < dist[v]) {
            dist[v] = tmp;
            pqueue.insert(multimap<int, int>::value_type(tmp, v));
          }
        }

        if (u - 1 >= 1) {
          int v = u - 1;
          int tmp = d + 1;
          if(tmp < dist[v]) {
            dist[v] = tmp;
            pqueue.insert(multimap<int, int>::value_type(tmp, v));
          }
        }
    }
}

int main () {
  cin >> N;
  for (int i = 1; i <= N; ++i) {
    cin >> a[i];
  }
  dijkstra();
  for (int i = 1; i <= N; ++i)
    cout << dist[i] << " ";
  cout << endl;
  return 0;
}
