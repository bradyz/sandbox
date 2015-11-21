#include <iostream>

using namespace std;

int N, T;
int values[1000001];

int main () {
    std::ios::sync_with_stdio(false);
    cin >> N >> T;
    values[0] = 0;
    int tmp;
    long long total = 0;
    for (int i = 1; i <= N; ++i) {
        cin >> tmp;
        if (tmp < T)
            values[i] = -1 + values[i-1];
        else
            values[i] = 1 + values[i-1];
    }
    // for (auto i: values)
    //     cout << i << "\t";
    // cout << endl;
    for (int i = 0; i <= N; ++i) {
        for (int j = i+1; j <= N; ++j) {
            if (values[j] - values[i] >= 0)
                ++total;
        }
    }
    cout << total << endl;
}
