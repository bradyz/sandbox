#include <iostream>
#include <cstring>

using namespace std;

int N;
bool grid[1001][1001];
int result;
int x1, y1, x2, y2;

int main () {
    while (cin >> N && N != 0) {
        result = 0;
        memset(grid, false, 1001*1001);
        for (int n = 0; n < N; ++n) {
            cin >> x1 >> y1 >> x2 >> y2;
            for (int i = 1; i+x1 <= x2; ++i)  {
                for (int j = 1; j+y1 <= y2; ++j) {
                    if (!grid[x1+i][y1+j])
                        result += 1;
                    grid[x1+i][y1+j] = true;
                }
            }
        }
        cout << result << endl;
    }
    return 0;
}
