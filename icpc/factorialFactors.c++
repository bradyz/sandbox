#include <iostream>
#include <cstring>
#include <cmath>

using namespace std;

int t;
int n;
int p[100001];
int c[100001];

int primeFactors (int x) {
    int r = 0;
    for (int i = 2; i <= sqrt(x); ++i) {
        while (x % i == 0) {
            x /= i;
            r += 1;
        }
    }
    if (x > 1)
        r += 1;
    return r;
}

void sieve () {
    memset(p, 0, sizeof(p));
    memset(c, 0, sizeof(c));


    for (int i = 0; i < 100001; ++i)
        p[i] = 1;

    p[0] = p[1] = 0;

    for (int i = 2; i < 100001; ++i) {
        if (p[i] == 0)
            continue;

        for (int j = i + i; j < 100001; j += i)
            p[j] = 0;
    }
    
    for (int i = 2; i < 100001; ++i) {
        p[i] += p[i-1];
        c[i] += primeFactors(i) + c[i-1];
    }
}

void solve (int x) {
    cout << p[x] << " " << c[x] << endl;
}

int main () {
    cin >> t;

    sieve();

    for (int i = 0; i < t; ++i) {
        cin >> n;
        solve(n);
    }
}
