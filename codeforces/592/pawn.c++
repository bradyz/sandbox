#include <iostream>
#include <string>
#include <algorithm>
#include <climits>

using namespace std;

char grid[8][8];
string row;
int minA = INT_MAX;
int minB = INT_MAX;

int dist (int x, int y) {
    int dir = grid[x][y] == 'W' ? -1 : 1;
    int result = 0;
    x += dir;
    while (x != -1 && x != 8) {
        if (grid[x][y] != '.')
            return INT_MAX;
        x += dir;
        result += 1;
    }
    return result;
}

int main () {
    for (int i = 0; i < 8; ++i) {
        cin >> row;
        for (int j = 0; j < 8; ++j)
            grid[i][j] = row[j];
    }
    for (int i = 0; i < 8; ++i) {
        for (int j = 0; j < 8; ++j) {
            if (grid[i][j] == 'W')
                minA = min(minA, dist(i, j));
            else if (grid[i][j] == 'B')
                minB = min(minB, dist(i, j));
        }
    }
    if (minA <= minB)
        cout << "A" << endl;
    else
        cout << "B" << endl;
    return 0;
}
