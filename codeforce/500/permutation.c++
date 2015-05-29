#include <iostream>

using namespace std;

int c[300];
char g[300][300];
int w[300];
int r[300];
bool u[300];
int n, x, cur;

void dfs(int i) {
    if(!u[c[i]])
        x = min(x, c[i]);

    w[i] = cur;

    for(int j = 0; j < n; ++j) {
        if(g[i][j] == '1' && w[j] != cur)
            dfs(j);
    }
}

int main() {
    cin >> n;

    for(int i = 0; i < n; ++i)
        cin >> c[i];

    for(int i = 0; i < n; ++i) {
        for(int j = 0; j < n; ++j) {
            cin >> g[i][j];
        }
    }

    for(int i = 0; i < n; ++i) {
        cur = i + 1;
        x = n;
        dfs(i);
        r[i] = x;
        u[x] = true;
        cout << r[i];

        if(i != n-1)
            cout << " ";
        else
            cout << endl;
    }
}
