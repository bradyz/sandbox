#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>

using namespace std;

int n, m;
int z;
int x, y;
vector<vector<char> > c;
unordered_map<int, vector<int> > v;
int depth[5000000];
char d[500000];
vector<int> t;

void dfs (int cur) {
    if (depth[cur] > y)
        return;
    else if (depth[cur] == y)
        t.push_back(cur);

    if (v.find(cur) == v.end())
        return;

    for (vector<int>::iterator it = v[cur].begin(); it != v[cur].end(); ++it) 
        dfs(*it);
}

string isPal () {
    int odds = 0;
    unordered_map<char, int> tmp;

    for (int i = 0; i < t.size(); ++i) {
        if (tmp.find(d[t[i]]) != tmp.end()) 
            tmp[d[t[i]]] += 1;
        else 
            tmp[d[t[i]]] = 1;
    }

    unordered_map<char, int>::iterator it;

    for (it = tmp.begin(); it != tmp.end(); ++it) {
        if (it->second % 2 == 1) {
            odds += 1;
            if (odds >= 2)
                return "No";
        }
    }

    return "Yes";
}

int main () {
    cin >> n >> m;

    depth[0] = 1;

    for (int i = 0; i < n-1; ++i) {
        cin >> z;
        depth[i+1] = depth[z-1] + 1;
        v[z-1].push_back(i+1);
    }
    
    for (int i = 0; i < n; ++i) 
        cin >> d[i];

    for (int i = 0; i < m; ++i) {
        cin >> x >> y;
        x -= 1;

        t.clear();
        dfs(x);

        cout << isPal() << endl;
    }

    return 0;
}
