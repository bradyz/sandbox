#include <iostream>
#include <string>
#include <map>
#include <set>

using namespace std;

int n;
string s;
set<char> m;
map<char, int> c[100005];

bool enough (int lo, int hi) {
    for (char x : m) {
        if (c[hi][x] - c[lo][x] == 0)
            return false;
    }
    return true;
}

int binary_search_left (int start) {
    int lo = start;
    int hi = n + 1;
    while (lo < hi) {
        int mi = (lo + hi) / 2;
        if (enough(start, mi))
            hi = mi;
        else
            lo = mi + 1;
    }
    return lo;
}

int main () {
    cin >> n;
    cin >> s;
    for (char t : s)
        m.insert(t);
    for (int i = 1; i <= n; ++i) {
        c[i] = c[i-1]; 
        c[i][s[i-1]] += 1;
    }
    int r = int(1e9);
    for (int i = 0; i <= n; ++i) {
        int x = binary_search_left(i);
        if (x < n + 1)
            r = min(r, x - i);
    }
    cout << r << endl;
}
