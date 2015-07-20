#include <iostream>

using namespace std;

int main() {
    int n;
    int c[6] = {100, 50, 20, 10, 5, 1};
    int d[6] = {0, 0, 0, 0, 0, 0};
    cin >> n;
    int i = 0;

    while(n > 0) {
        while(n - c[i] >= 0) {
            n -= c[i];
            d[i] += 1;
        }
        if(n == 0)
            break;
        i += 1;
    }

    for(int j = 0; j < 6; ++j) {
        if(d[j] != 0) {
            cout << c[j] << " " << d[j] << endl;
        }
    }
}
