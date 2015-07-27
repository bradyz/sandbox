#include <iostream>
#include <algorithm>
#include <sstream>

using namespace std;

int g[1000][1000];
int n, m;

int main() {
    int x, y;
    int a, b;
    int r = 0;
    string t;
    cin >> m;
    cin >> n;

    for(int i = 0; i < n; ++i) {
        cin >> t;
        for(int j = 0; j < m; ++j)
            g[i][j] = t[j] - '0';
    }

    for(int i = 0; i < n; ++i) {
        for(int j = 0; j < m; ++j) {
            int t = g[i][j];
            for(int k = 1; k < min(m-j, n-i); ++k) {
                int l = 0;
                while(l < k && g[i+l][j]==t && g[i][j+l]==t && g[i+k][j+l]==t && g[i+l][j+k]==t)
                    l += 1;
                if(l >= k && l > r ){
                    r = l;                    
                    x = i;
                    y = j;
                    a = i+l;
                    b = j+l;
                }
            }
        }
    }

    cout << g[x][y] << endl;
    cout << x << "," << y << endl;
    cout << a << "," << b << endl;
}
