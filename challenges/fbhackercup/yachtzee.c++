#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

const float EPS = 1e-5;

int T;
int N, A, B;
float cost[100005];

float left_over(float x) {
    if (x >= cost[N-1])
        return left_over(x - cost[N-1]);
    float i = upper_bound(cost, cost + N, x) - cost;
    if (i == 0)
        return x;
    return x - cost[int(i)-1];
}

int main () {
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        scanf("%d %d %d", &N, &A, &B);
        for (int i = 0; i < N; ++i) {
            scanf("%f", cost + i);
            if (i != 0)
                cost[i] += cost[i-1];
        }
        float result = 0;
        for (float x = A; x <= B; ++x) {
            if (x != A)
                result += left_over(x - EPS);
            if (x != B)
                result += left_over(x + EPS);
        }
        printf("%f\n", result / (2 * B - 2 * A));
    }
    return 0;
}
