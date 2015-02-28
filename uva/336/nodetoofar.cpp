#include <iostream>
#include <vector>
#include <map>
#include <queue>
#include <unordered_set> // size, find, insert, erase
#include <string>
#include <cstdio> // scanf

using namespace std;

int tmp;
vector <int> tmpv;
queue <int> q;
map <int, int> v;

int reach(map <int, vector <int> > &graph, int start, int jump) {
    tmpv.clear();
    q.empty();
    v.clear();

    for(map <int, vector <int> >::iterator it = graph.begin(); it != graph.end(); ++it) 
        v[it->first] = -1;

    q.push(start);
    v[start] = jump;

    while(!q.empty()) {
        tmp = q.front();
        q.pop();
        tmpv = graph[tmp];
        for(vector <int>::iterator it = tmpv.begin(); it != tmpv.end(); ++it) {
            if(v[tmp] - 1 > v[*it]) {
                // cout << *it << " " << v[tmp] - 1 << endl;
                v[*it] = v[tmp] - 1;
                q.push(*it);
            }
        }
    }

    int count = 0;

    for(map <int, int>::iterator it = v.begin(); it != v.end(); ++it) 
    {
        // cout << it->first << " " << it->second << endl;
        if(it->second > -1)
            count += 1;
    }
        

    return graph.size() - count;
}

int main() {
    int n;
    int a, b;
    int s, e;
    int c = 0;
    int res = 0;

    while(scanf("%d", &n) && n) {
        map <int, vector<int> > g;
        for(int i = 0; i < n; ++i) {
            scanf("%d %d", &a, &b);
            g[a].push_back(b);
            g[b].push_back(a);
        }

        while(scanf("%d %d", &s, &e) && (s != 0 || e != 0)) {
            res = reach(g, s, e);
            cout << "Case " << ++c << ": " << res << " nodes not reachable from node ";
            cout << s << " with TTL = " << e << "." << endl;
        }
    }
}
