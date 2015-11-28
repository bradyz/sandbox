#include <iostream>
#include <vector>

using namespace std;

int K, N;
vector<long long> R;

int main () {
    cin >> K >> N;
    for (int k = 0; k < K; ++k) {
        long long tmp;
        cin >> tmp;
        R.push_back(tmp);
    }
    long long total = 0;
    for (int n = 0; n < N; ++n) {
        long long x, y;
        cin >> x >> y;
        for (int i = K-1; i >= 0; --i) {
            if (x * x + y * y <= R[i] * R[i]) {
                total += i+1;
                break;
            }
        }
    }
    cout << total << endl;
    return 0;
}
