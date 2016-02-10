#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

#define MAX_N 1000

double problem1 (double x) {
    return pow(x, 2) + 10 * cos(x);
}

double problem2 (double x) {
    return pow(x, 4) - 3 * pow(x, 2) - 3;
}

double problem4 (double x) {
    return tan(x);
}

double bisection (double (*func)(double), double po, double thresh, double a, double b, int iterations=MAX_N) {
    double pi = po;
    for (int i = 1; i <= iterations; ++i) {
        cout << "i: " << i << " ";
        cout << "p: " << pi << " " << "f(p): " << func(pi) << endl;
        pi = func(po);
        if (pi < a)
            pi = a;
        else if (pi > b)
            pi = b;
        if (abs(pi - po) < thresh)
            break;
        po = pi;
    }
    return pi;
}

int main () {
    bisection(problem1, 3.6, 0, 3, 4, 4);
    cout << endl;
    bisection(problem2, 1, 0, 1, 2, 5);
    cout << endl;
    bisection(problem4, 4.5, 1e-5, 4, 5, 2);
    return 0;
}
