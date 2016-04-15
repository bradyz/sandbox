#include <iostream>
#include <omp.h>
#include <set>

using namespace std;

const int N = 10000;

int a[N][N];
int b[N][N];

int main () {
    int H = 500;
    int W = 600;
    int c = 0;

    for (int i = 0; i < H; ++i) 
        for (int j = 0; j < W; ++j)
            a[i][j] = ++c;

    for (int i = 0; i < H; ++i)
        for (int j = 0; j < W; ++j)
            cout << a[i][j] << " ";
    cout << endl;

    int split = 2;

#pragma mp parallel for collapse(2)
    for (int i = 0; i < H; i += H / split) {
        for (int j = 0; j < W; j += W / split) {
            for (int x = 0; x < H / split; ++x) {
                for (int y = 0; y < W / split; ++y) {
                    b[i+x][j+y] = a[i+x][j+y];
                }
            }
        }
    }

    set<int> s;

    for (int i = 0; i < H; ++i)
        for (int j = 0; j < W; ++j)
            s.insert(b[i][j]);

    cout << s.size() << endl;

    return 0;
}
