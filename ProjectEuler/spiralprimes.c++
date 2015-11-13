#include <iostream>
#include <cstring>

using namespace std;

#define MAX_N 1000000001

bool primes[MAX_N];
int idx[] = {2, 4, 6, 8};
int cur[] = {1, 1, 1, 1};

int main () {
    memset(primes, true, sizeof(primes));
    primes[0] = primes[1] = false;
    for (int i = 2; i < MAX_N; ++i) {
        if (!primes[i]) continue;
        for (int j = i + i; j < MAX_N; j += i)
            primes[j] = false;
    }
    int layer = 1;
    double num = 0;
    while (layer == 1 || (num) / (4 * (layer-1) + 1) >= .1) {
        for (int i = 0; i < 4; ++i) {
            if (primes[cur[i]+idx[i]])
                ++num;
            cur[i] += idx[i];
            idx[i] += 8;
        }
        layer += 1;
    }
    cout << 2*layer-1 << endl;
    return 0;
}
