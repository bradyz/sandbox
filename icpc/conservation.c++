#include <iostream>
#include <vector>
#include <unordered_map>
#include <cstring>
#include <queue>

using namespace std;

int t, ct;
int n, m;
unordered_map<int, vector<int> > graph;
int values[100001];

int solve (queue<int> fac1, queue<int> fac2, vector<int> occur, int ob) {
    int r1 = 0;
    int obs = ob;
    int cur;

    // start with fac1
    while (fac1.size() > 0 || fac2.size() > 0) {
        if (obs == 1) {
            if (fac1.size() > 0) {
                cur = fac1.front();
                fac1.pop();
            }
            else {
                cur = fac2.front();
                fac2.pop();
                obs = 1 + (obs % 2);
                r1 += 1;
            }
        }
        else {
            if (fac2.size() > 0) {
                cur = fac2.front();
                fac2.pop();
            }
            else {
                cur = fac1.front();
                fac1.pop();
                obs = 1 + (obs % 2);
                r1 += 1;
            }
        }

        // cout << cur << endl;

        for (auto it: graph[cur]) {
            occur[it] -= 1;             
            if (occur[it] == 0) {
                if (values[it] == 1)
                    fac1.push(it);
                else
                    fac2.push(it);  
                // cout << "pushed: " << it << " " << r1 << endl;
            }
        }
    }
    // cout << "output: " << r1 << endl;
    return r1;
}

void topo (vector<int> &occur) {
    queue<int> fac1;
    queue<int> fac2;

    for (int i = 1; i <= n; ++i) {
        if (occur[i] == 0) {
            if (values[i] == 1)
                fac1.push(i);
            else
                fac2.push(i);
        }
    }

    cout << min(solve(fac1, fac2, occur, 1), solve(fac1, fac2, occur, 2)) << endl;
}

int main () {
    int x, y;

    cin >> t;

    for (ct = 0; ct < t; ++ct) {
        graph.clear();

        cin >> n >> m;

        vector<int> occur(n+1);

        for (int i = 1; i <= n; ++i)
            cin >> values[i];

        for (int i = 0; i < m; ++i) {
            cin >> x >> y;

            occur[y] += 1;
            graph[x].push_back(y);
        }

        topo(occur);
    }

    return 0;
}
