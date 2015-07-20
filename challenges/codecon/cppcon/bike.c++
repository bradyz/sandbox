#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

int n, m;
int x, y;
int r;
vector<pair<int, int> > c;

int dfs(int i, int d, int f) {
    if(f < 0)
        return 100001;

    cout << c[i].first << " " << c[i].second << " " << d << " " << f << endl;

    if(f >= d)
        return 0;
    
    int t = 100001;

    for(int j = i-1; j >= 0; --j) {
       t = min(t, dfs(j, c[j].first, f+c[j].second-(d-c[j].first))+1);
    }

    return t;
}

int main() {
    m = 100001;
    cin >> n;

    for(int i = 0; i < n; ++i) {
        cin >> x >> y;
        pair<int, int>t(x, y);
        c.push_back(t);
    }

    cin >> x >> y;

    int t = min(dfs(n, x, y), m);
    if(t == 100001) {
        cout << -1 << endl;
    }
    else {
        cout << t << endl;
    }
}
