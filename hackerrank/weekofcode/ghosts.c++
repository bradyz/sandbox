#include <iostream>

using namespace std;

int A, B, C, D;

int gcd (int a, int b) {
    if (a == 0)
        return b;
    return gcd(b % a, a);
}

int main () {
    cin >> A >> B >> C >> D;
    long long total = 0;
    for (int a = 1; a <= A; ++a) {
        for (int b = 1; b <= B; ++b) {
            for (int c = 1; c <= C; ++c) {
                for (int d = 1; d <= D; ++d) {
                    bool r = true;
                    r &= (a - b) % 3 == 0;
                    r &= (b + c) % 5 == 0;
                    r &= (a * c) % 4 == 0;
                    r &= gcd(a, d) == 1;
                    total += r;
                }
            }
        }
    }
    cout << total << endl;
    return 0;
}
