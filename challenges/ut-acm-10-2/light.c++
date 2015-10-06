#include <iostream>
#include <string>
#include <vector>
#include <utility>
#include <cstring>

using namespace std;

int t;
int m, n;
int r;

bool ga[20][20];
bool gb[60][60];

vector<pair<int, int> > tv;
vector<pair<int, int> > cv;

void solve () {

}

int main () {
    int dx[] = {0, 0, 0, 1, 1, 1, 2, 2, 2};
    int dy[] = {0, 1, 2, 0, 1, 2, 0, 1, 2};
    string s;
    cin >> t;
    for (int ct = 0; ct < t; ++ct) {
        cin >> m >> n;
        memset(ga, false, sizeof(bool) * m * n);
        memset(gb, false, sizeof(bool) * m * n * 3 * 3);
        tv.clear();
        for (int mi = 0; mi < m; ++mi) {
            cin >> s;
            for (int ci = 0; ci < n; ++ci) {
                ga[mi][ci] = s[ci] == '#';
                for (int i = 0; i < 9; ++i)
                    gb[mi*3+dx[i]][ci*3+dy[i]] |= s[ci] == '#';
                if (s[ci] == '#')
                    tv.push_back(pair<int, int>(mi, ci)); 
            }
        }
    }

    solve();
}
