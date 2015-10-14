#include <iostream>
#include <utility>
#include <cstring>
#include <string>
#include <algorithm>

using namespace std;

int n;
int c[1001][1001];
int dp1[1001][1001];
int dp2[1001][1001];
pair<int, int> p1[1001][1001];
pair<int, int> p2[1001][1001];

int num (int x, int k) {
    int r = 0;
    while (x != 0 && x % k == 0) {
        x /= k;
        r += 1;
    }
    return r;
}

int main () {
    cin >> n;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> c[i][j];
            dp1[i][j] = num(c[i][j], 5);
            dp2[i][j] = num(c[i][j], 2);
        }
    }
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (i == 0 && j == 0) 
                continue;
            else if (i == 0) {
                dp1[i][j] += dp1[i][j-1];
                dp2[i][j] += dp2[i][j-1];
                p1[i][j] = pair<int, int>(i, j-1);
                p2[i][j] = pair<int, int>(i, j-1);
            }
            else if (j == 0) {
                dp1[i][j] += dp1[i-1][j];
                dp2[i][j] += dp2[i-1][j];
                p1[i][j] = pair<int, int>(i-1, j);
                p2[i][j] = pair<int, int>(i-1, j);
            }
            else {
                if (dp1[i-1][j] < dp1[i][j-1]) {
                    dp1[i][j] += dp1[i-1][j] ;
                    p1[i][j] = pair<int, int>(i-1, j);
                } 
                else {
                    dp1[i][j] += dp1[i][j-1] ;
                    p1[i][j] = pair<int, int>(i, j-1);
                }
                if (dp2[i-1][j] < dp2[i][j-1]) {
                    dp2[i][j] += dp2[i-1][j] ;
                    p2[i][j] = pair<int, int>(i-1, j);
                } 
                else {
                    dp2[i][j] += dp2[i][j-1] ;
                    p2[i][j] = pair<int, int>(i, j-1);
                }
            }
        }
    }
    int r = 0;
    string path = "";
    pair<int, int> p(n-1, n-1);
    if (dp1[n-1][n-1] < dp2[n-1][n-1]) {
        while (p.first != 0 || p.second != 0) {
            r += num(c[p.first][p.second], 2);
            if (p1[p.first][p.second].first < p.first)
                path += "D";
            else
                path += "R";
            p = p1[p.first][p.second];
        }
        r += num(c[0][0], 2);
    }
    else {
        while (p.first != 0 || p.second != 0) {
            r += num(c[p.first][p.second], 5);
            if (p2[p.first][p.second].first < p.first)
                path += "D";
            else
                path += "R";
            p = p2[p.first][p.second];
        }
        r += num(c[0][0], 5);
    }
    reverse(path.begin(), path.end());
    cout << min(r, min(dp1[n-1][n-1], dp2[n-1][n-1])) << endl;
    cout << path << endl;
    return 0;
}
