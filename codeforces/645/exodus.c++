#include <iostream>
#include <vector>

using namespace std;

int n, k;
char r[100005];
int s[100005];

int main () {
    cin >> n >> k >> r;
    int x = 0;
    for (int i = 0; i < n; ++i) {
        if (r[i] == '0')
            s[x++] = i;
    }
    vector<int> b;
    int d = int(1e9);
    b.push_back(0);
    for (int i = 0; i <= k; ++i) {
        if (max(s[i] - s[0], s[k] - s[i]) <= d) {
            if (max(s[i] - s[0], s[k] - s[i]) < d)
                b.clear();
            b.push_back(i);
            d = max(s[i] - s[0], s[k] - s[i]);
        }
    }
    // cout << d << endl;
    // for (int p: b)
    //     cout << s[p] << " ";
    // cout << endl;
    int ret = int(1e9);
    for (int i = k; i < x; ++i) {
        for (int j = 0; j < b.size(); ++j) {
            int p = b[j];
            // cout << s[i-k] << " " << s[p] << " " << s[i] << endl;
            ret = min(ret, max(s[p] - s[i-k], s[i] - s[p]));
            ++b[j];
        }
    }    
    cout << ret << endl;
    return 0;
}
