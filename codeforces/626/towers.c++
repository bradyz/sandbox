#include <iostream>
#include <unordered_set>

using namespace std;

int n, m;

int main () {
    cin >> n >> m;
    unordered_set<int> num;
    int ret = 0;
    for (int i = 1; i <= m; ++i) {
        num.insert(i * 3);
        ret = max(ret, i * 3);
    }
    int ni = 1;
    for (int i = 0; i < n; ++i) {
        while (num.find(ni * 2) != num.end())
            ++ni;
        num.insert(ni * 2);
        ret = max(ret, ni * 2);
    }
    cout << ret << endl;
}
