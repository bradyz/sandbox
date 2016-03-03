#include <iostream>
#include <vector>

using namespace std;

bool v[5005][5005];
int col[5005][5005];
bool ro[5005];
bool co[5005];

int n, m, k;
int q;

int main () {
    cin >> n >> m >> k;
    vector<vector<int> > queries;
    for (int i = 0; i < k; ++i) {
        int a, b, c;
        cin >> a >> b >> c;
        vector<int> tmp;
        tmp.push_back(a);
        tmp.push_back(b);
        tmp.push_back(c);
        queries.push_back(tmp);
    }
    for (int i = queries.size()-1; i >= 0; --i) {
        int a, b, c;
        a = queries[i][0];
        b = queries[i][1]-1;
        c = queries[i][2];
        if (a == 1) {
            if (ro[b])
                continue;
            ro[b] = true;
            for (int j = 0; j < m; ++j) {
                if (v[b][j])
                    continue;
                v[b][j] = true;
                col[b][j] = c;
            }
        }
        else {
            if (co[b])
                continue;
            co[b] = true;
            for (int j = 0; j < n; ++j) {
                if (v[j][b])
                    continue;
                v[j][b] = true;
                col[j][b] = c;
            }
        }
    }

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cout << col[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}
