#include <iostream>
#include <vector>

using namespace std;

struct interval {
    int a, b;
    interval (int c, int d) : a(c), b(d) {}
    bool operator== (interval& other) {
        return a == other.a && b == other.b;
    }
};

int N;
vector<interval> intervals;

bool dfs (interval& i1, interval& i2, vector<bool>& vis) {
    if (i1 == i2)
        return true;
    for (int i = 0; i < intervals.size(); ++i) {
        if (vis[i])
            continue;
        if ((intervals[i].a < i1.a && i1.a < intervals[i].b) ||
                (intervals[i].a < i1.b && i1.b < intervals[i].b)) {
            vis[i] = true;
            if (dfs(intervals[i], i2, vis))
                return true;
        }
    }
    return false;
}

int main () {
    int x, y;
    int a, b;
    int q;

    cin >> N;

    for (int i = 0; i < N; ++i) {
        cin >> q;
        if (q == 1) {
            cin >> x >> y;
            intervals.push_back(interval(x, y));
        }
        else {
            cin >> a >> b;
            vector<bool> vis(intervals.size(), false);
            if (dfs(intervals[a-1], intervals[b-1], vis))
                cout << "YES" << endl;
            else
                cout << "NO" << endl;
        }
    }
    return 0;
}
