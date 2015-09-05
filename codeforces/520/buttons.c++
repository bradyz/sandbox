#include <iostream>
#include <utility>
#include <queue>
#include <set>

using namespace std;

int n, m;
queue<pair<int, int> > q;
pair<int, int> c;
set<int> d;

int main () {
    cin >> n >> m;

    q.push(pair<int, int>(n, 0));

    while (q.size() > 0) {
        c = q.front();
        q.pop();

        if (d.find(c.first) != d.end())
            continue;

        d.insert(c.first);

        if (c.first == m) {
            cout << c.second << endl;
            break;
        }

        if (c.first > 0)
            q.push(pair<int, int>(c.first - 1, c.second + 1));

        if (c.first < m * 2) 
            q.push(pair<int, int>(c.first * 2, c.second + 1));
    }

    return 0;
}
