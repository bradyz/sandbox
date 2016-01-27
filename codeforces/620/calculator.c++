#include <iostream>

using namespace std;

int A, B;
int segments[] = {6, 2, 5, 5, 4, 5, 6, 3, 7, 6};

int main () {
    cin >> A >> B;
    int ret = 0;
    for (int x = A; x <= B; ++x) {
        int y = x;
        while (y > 0) {
            ret += segments[y % 10];
            y /= 10;
        }
    }
    cout << ret << endl;
    return 0;
}
