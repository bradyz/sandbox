#include <cstdio>
#include <iostream>
#include <vector>
#include <unordered_set>
#include <unordered_map>
#include <string>
#include <sstream>
#include <algorithm>
#include <queue>

using namespace std;

int T;
int n;
unordered_map<int, vector<int> > g;
unordered_map<string, int> l;
unordered_set<int> v;

int dfs (int u) {
    if (v.find(u) != v.end())
        return 0;
    v.insert(u);
    int r = 1;
    for (int d : g[u]) {
        r += dfs(d);
    }
    return r;
}

void solve () {
    int r = int(1e9);
    for (auto it : g) {
        v.clear();
        r = min(r, dfs(it.first));
    }
    cout << r << endl;
}

int main () {
    ios::sync_with_stdio(0);
    cin >> T;
    while (T--) {
        g.clear();
        l.clear();
        cin >> n;
        string s, u, v;
        for (int i = 0; i <= n; ++i) {
            getline(cin, s);
            if (i == 0) continue;
            stringstream ss(s);
            ss >> u;
            if (l.find(u) == l.end())
                l[u] = l.size();
            int x = l[u];
            g[x] = vector<int>();
            while (ss >> v) {
                if (l.find(v) == l.end())
                    l[v] = l.size();
                int y = l[v];
                g[x].push_back(y);
            }
        }
        solve();
    }
    return 0;
}
