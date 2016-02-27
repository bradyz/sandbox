#include <iostream>

using namespace std;

int N;

int main () {
    cin >> N;
    unsigned long long ret = 1;
    ret += (N * N + N) * 3;
    cout << ret << endl;
    ret = 1;
    for (int i = 1; i <= N; ++i)
        ret += i * 6;
    cout << ret << endl;
}
