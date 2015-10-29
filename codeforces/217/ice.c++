#include <iostream>
#include <vector>
#include <unordered_set>
#include <cstring>

using namespace std;

struct point {
    int x, y;
    point (int a, int b) : x(a), y(b) {};
};

int N;
vector<point> points;
int par[101];

int root (int v) {
    return par[v] < 0 ? v : (par[v] = root(par[v]));
}

void merge (int x,int y) {
    if((x = root(x)) == (y = root(y)))
        return;
    if(par[y] < par[x])
        swap(x, y);
    par[x] += par[y];
    par[y] = x;
}

int main () {
    cin >> N;

    for (int i = 0; i < N; ++i) {
        int x, y;
        cin >> x >> y;
        points.push_back(point(x, y));
    }

    memset(par, -1, sizeof(par) / sizeof(bool));

    for (int i = 0; i < N; ++i) {
        for (int j = i+1; j < N; ++j) {
            if (points[i].x == points[j].x || points[i].y == points[j].y)
                merge(i, j);
        }
    }

    unordered_set<int> roots;

    for (int i = 0; i < N; ++i)
        roots.insert(root(i));
    
    cout << roots.size()-1 << endl;
}
