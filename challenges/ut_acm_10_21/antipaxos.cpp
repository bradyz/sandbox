#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

int T;
int n;
map<string, vector<string> > g;

void print (map<string, vector<string> > g) {
    for (auto it : g) {
        cout << it.first << ": ";
        for (auto it1 : it.second) {
            cout << it1 << " ";
        }
        cout << endl;
    }
}

void dfs (string u, set<string>& v, map<string, vector<string> >& g, vector<string>& o) {
    if (v.find(u) != v.end())
        return;
    v.insert(u);
    for (string to : g[u]) {
        dfs(to, v, g, o);
    }
    o.push_back(u);
}

void solve () {
    set<string> v;
    vector<string> r;
    map<string, vector<string> >::iterator it;
    for (it = g.begin(); it != g.end(); ++it) {
        dfs(it->first, v, g, r);
    }
    reverse(r.begin(), r.end());


    map<string, vector<string> > gr;
    set<string> v1;

    for (it = g.begin(); it != g.end(); ++it) {
        if (gr.find(it->first) == gr.end())
            gr[it->first] = vector<string>();
        for (string s : it->second) {
            if (gr.find(s) == gr.end())
                gr[s] = vector<string>();
            gr[s].push_back(it->first);
        }
    }

    // print(g);
    // print(gr);
    vector<string> ans;
    for (string u : r) {
        vector<string> scc;
        dfs(u, v1, gr, scc);
        if (scc.size() > 0) {
            ans = scc;
        }
    }

    cout << ans.size() << endl;
    //
    // for (vector<string> scc : sccs) {
    //     for (string s : scc)
    //         cout << s << " ";
    //     cout << endl;
    // }
}

int main () {
    cin >> T;
    while (T--) {
        g.clear();

        cin >> n;

        string s, u, v;
        for (int i = 0; i <= n; ++i) {
            getline(cin, s);
            if (i == 0)
                continue;
            stringstream ss(s);
            ss >> u;
            g[u] = vector<string>();
            while (ss >> v) {
                g[u].push_back(v);
            }
        }

        solve();
    }
    return 0;
}
