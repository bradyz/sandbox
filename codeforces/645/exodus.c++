#include <iostream>
#include <string>

using namespace std;

int n, k;
string r;
int s[100005];

int main () {
    cin >> n >> k >> r;
    int x = 0;
    for (int i = 0; i < n; ++i) {
        if (r[i] == '0')
            s[x++] = i;
    }
    int win = int(1e9);
    int ret = int(1e9);
    for (int i = k; i < x; ++i) {
        if (s[i] - s[i-k] > win)
            continue;
        win = s[i] - s[i-k];
        for (int j = i-k; j < i; ++j)
            ret = min(ret, max(s[j] - s[i-k], s[i] - s[j]));
    }    
    cout << ret << endl;
    return 0;
}
