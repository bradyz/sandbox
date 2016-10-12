#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

int N;
double vessels[1001][4];

void pretty (double t) {
    cout << int(t) << " hour(s) ";
    t -= int(t);
    t *= 60;
    cout << int(t) << " minute(s) ";
    t -= int(t);
    t *= 60;
    cout << ceil(t) << " second(s)" << endl;
}

double amount (double x, double y, double s, double vx, double vy, double vvx, double vvy) {
    double a = vvx * vvx + vvy * vvy - s * s;
    double b = 2.0 * vvx * (vx - x) + 2.0 * vvy * (vy - y);
    double c = (vx - x) * (vx - x) + (vy - y) * (vy - y);

    if (b * b - 4.0 * a * c < 0.0)
        return double(1e9);

    double t1 = (-b + sqrt(b * b - 4.0 * a * c)) / (2.0 * a);
    double t2 = (-b - sqrt(b * b - 4.0 * a * c)) / (2.0 * a);

    if (t1 < 0.0)
        return t2;
    else if (t2 < 0.0)
        return t1;

    return min(t1, t2);
}

double solve (vector<int>& perm, double x, double y, double s) {
    double t = 0.0;
    for (int i : perm) {
        double vx = vessels[i][0] + t * vessels[i][2];
        double vy = vessels[i][1] + t * vessels[i][3];
        double vvx = vessels[i][2];
        double vvy = vessels[i][3];

        double dt = amount(x, y, s, vx, vy, vvx, vvy) + 1.0;

        x = vx + dt * vvx;
        y = vy + dt * vvy;

        t += dt;
    }
    return t + sqrt(x * x + y * y) / s;
}

int main () {
    cin >> N;
    int t = 1;

    while (N != 0) {
        for (int i = 0; i < N; ++i)
            for (int j = 0; j < 4; ++j)
                cin >> vessels[i][j];

        double x, y, s;
        cin >> x >> y >> s;

        vector<int> perm;
        for (int i = 0; i < N; ++i)
            perm.push_back(i);
        sort(perm.begin(), perm.end());

        double result = 1e10;
        do {
            result = min(result, solve(perm, x, y, s));
        } while (next_permutation(perm.begin(), perm.end()));

        cout << "Case " << t << ": ";
        pretty(result);

        t += 1;
        cin >> N;
    }

    return 0;
}
