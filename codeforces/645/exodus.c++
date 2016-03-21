#include <iostream>
#include <vector>

using namespace std;

int s[100005];
char r[100005];

int n, k;

int main () {
    cin >> n >> k >> r;
    int x = 0;
    for (int i = 0; i < n; ++i) {
        if (r[i] == '0')
            s[x++] = i;
    }
    int p = 0;
    for (int i = 0; i <= k; ++i) {
        if (max(s[i] - s[0], s[k] - s[i]) < max(s[p] - s[0], s[k] - s[p])) 
            p = i;
    }
    int ret = int(1e9);
    for (int i = k; i < x; ++i) {
        while (p + 1 < x && max(s[p+1]-s[i-k], s[i]-s[p+1]) < max(s[p]-s[i-k], s[i]-s[p]))
            ++p;
        ret = min(ret, max(s[p] - s[i-k], s[i] - s[p]));
    }    
    cout << ret << endl;
    return 0;
}
