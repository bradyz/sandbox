#include <iostream>
#include <unordered_set>
#include <vector>

using namespace std;

int main() {
    int n, m, tmp;
    int dp[100000];
    string input;

    cin >> n >> m;

    vector<int> a(n, 0);

    for(int i = 0; i < n; ++i) {
        cin >> tmp;
        a[i] = tmp;
    }

    unordered_set<int> dis;

    dis.insert(a[n-1]);

    dp[n-1] = 1;

    for(int i = n-2; i >= 0; --i) {
        if(dis.find(a[i]) == dis.end()) {
            dp[i] = dp[i+1] + 1;
            dis.insert(a[i]);
        }
        else 
            dp[i] = dp[i+1];
    }

    for(int i = 0; i < m; ++i) {
        cin >> tmp;
        cout << dp[tmp-1] << endl;
    }

    return 0;
}
