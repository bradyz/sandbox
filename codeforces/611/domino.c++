#include <cstdio>

#define MAX_N 505

using namespace std;

int h, w;
char grid[MAX_N][MAX_N];
int ver[MAX_N][MAX_N];
int hor[MAX_N][MAX_N];
int q;
int r1, c1, r2, c2;

int main () {
    scanf("%d %d", &h, &w);
    for (int i = 1; i <= h; ++i)
        scanf("%s", grid[i] + 1);
    for (int i = 1; i <= h; ++i) {
        for (int j = 1; j <= w; ++j) {
            ver[i][j] = ver[i-1][j] + ver[i][j-1] - ver[i-1][j-1];
            hor[i][j] = hor[i-1][j] + hor[i][j-1] - hor[i-1][j-1];
            if (grid[i][j] == '.' && grid[i][j-1] == '.')
                ++hor[i][j];
            if (grid[i][j] == '.' && grid[i-1][j] == '.')
                ++ver[i][j];
        }
    }
    scanf("%d", &q);
    while (q--) {
        scanf("%d %d %d %d", &r1, &c1, &r2, &c2);
        int answer = 0;
        answer += ver[r2][c2] - ver[r1][c2] - ver[r2][c1-1] + ver[r1][c1-1];
        answer += hor[r2][c2] - hor[r2][c1] - hor[r1-1][c2] + hor[r1-1][c1];
        printf("%d\n", answer);
    }
    return 0;
}
