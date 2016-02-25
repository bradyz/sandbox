#include <iostream>

#define MOD 1000000007;

using namespace std;

int N;

int main () {
    cin >> N;
    long long ret = 1;
    long long abc = 0;
    for (int i = 1; i <= N; ++i) {
        long long tmpRet = (abc * 3) % MOD;
        long long tmp = (ret + 2ll * abc) % MOD;
        ret = tmpRet;
        abc = tmp;
    }
    cout << ret << endl;
    return 0;
}
