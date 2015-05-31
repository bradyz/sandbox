#include <iostream>
#include <queue>
#include <string>
#include <utility>

using namespace std;

char arr[500][500];
int n, m;
int s_x, s_y;
int e_x, e_y;
int x, y;

void print_arr() {
    for(int i = 0; i < n; ++i) {
        for(int j = 0; j < m; ++j) {
            cout << arr[i][j];
        }
        cout << endl;
    }
}

int main() {
    queue<pair<int, int> > q;
    pair<int, int> cur(-1, -1);
    bool okay = false;

    cin >> n >> m;

    for(int i = 0; i < n; ++i) {
        for(int j = 0; j < m; ++j) { 
            cin >> arr[i][j];
        }
    }

    cin >> s_x >> s_y;
    cin >> e_x >> e_y;

    arr[s_x-1][s_y-1] = '.';
    q.push(pair<int, int>(s_x-1, s_y-1));

    while(!q.empty()) {
        pair<int, int> cur = q.front();
        q.pop();
        x = cur.first;
        y = cur.second;
        if(x >= 0 && x < n && y >= 0 && y < m) {
            if(arr[x][y] == '.') { 
                arr[x][y] = 'X';
                q.push(pair<int, int>(x-1, y));
                q.push(pair<int, int>(x+1, y));
                q.push(pair<int, int>(x, y+1));
                q.push(pair<int, int>(x, y-1));
            }
            else if(x + 1 == e_x && y + 1 == e_y) {
                okay = true;
                break;
            }
        }
    }


    cout << (okay ? "YES" : "NO") << endl;
}
