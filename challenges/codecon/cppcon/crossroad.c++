#include <iostream>
#include <sstream>
#include <unordered_set>
#include <utility>
#include <string>
#include <vector>
#include <algorithm>


using namespace std;

int g[1000][1000];
int n, m;
int r;

struct pair_hash {
    inline std::size_t operator()(const std::pair<int,int> & v) const {
        return v.first*10001+v.second;
    }
};

void dfs(int i, int j, vector<pair<int, int> > v) {
    if(find(v.begin(), v.end(), pair<int, int>(i, j)) != v.end())
        return;
    if(i < 0 || j < 0 || i >= n || j >= m || g[i][j] == 0)
        return;
    if(i == n-1 && j == m-1 && g[i][j] == 1) {
        // for(auto it = v.begin(); it != v.end(); ++it) {
        //     cout << it-> first << " " << it->second << endl;
        // }
        // cout << endl;
        r += 1;
        return;
    }    
    v.push_back(pair<int, int>(i, j));
    dfs(i+1, j, v);
    dfs(i, j+1, v);
}

int main() {
    r = 0;

    cin >> n;
    cin >> m;


    for(int i = 0; i < n; ++i) {
        for(int j = 0; j < m; ++j) {
            int t;
            cin >> t;
            g[i][j] = t;
        }
    }

    vector<pair<int, int> >t;
    dfs(0, 0, t);

    cout << r << endl;
}
