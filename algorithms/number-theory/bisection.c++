#include <iostream>
#include <cmath>

using namespace std;

float foo (float x) {
    return sqrt(x) - cos(x);
}

float bisection (float (*func)(float), float a, float b, float thresh) {
    int k = 0;
    float error = b - a;
    float a_k = a;
    float b_k = b;
    float c_k;

    while (error > thresh) {
        c_k = (b_k + a_k) / 2.0f;
        cout << "x: " << c_k << " val: " << func(c_k);
        cout << " iteration: " << k << " error: " << error << endl;
        if (func(c_k) < 0)
            a_k = c_k;
        else
            b_k = c_k;
        error /= 2;
        ++k;
    }

    return c_k;
}

int main () {
    bisection(foo, 0, 1, 10e-5);
    return 0;
}
