#include <iostream>
#include <cassert>
#include <map>
#include <algorithm>
#include <utility>
#include <vector>

using namespace std;

typedef pair<int, int> pii;
typedef long long ll;

int n, m;
ll a[2005];
ll b[2005];

int main () {
    ll a_sum = 0;
    ll b_sum = 0;
    cin >> n;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        a_sum += a[i];
    }
    cin >> m;
    for (int i = 0; i < m; ++i) {
        cin >> b[i];
        b_sum += b[i];
    }
    vector<pii> ret;
    ll ret_val = abs(a_sum - b_sum);
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            ll new_a_sum = a_sum - a[i] + b[j];
            ll new_b_sum = b_sum - b[j] + a[i];
            if (ret_val > abs(new_a_sum - new_b_sum)) {
                ret_val = abs(new_a_sum - new_b_sum);
                ret.clear();
                ret.push_back(pii(i, j));
            }
        }
    }
    map<ll, pii> pair_val;
    for (int i = 0; i < n; ++i)
        for (int j = i+1; j < n; ++j)
            pair_val[a[i] + a[j]] = pii(i, j);
    for (int i = 0; i < m; ++i) {
        for (int j = i+1; j < m; ++j) {
            int a_pair = (a_sum - b_sum + 2 * (b[i] + b[j])) / 2;
            assert((a_sum - b_sum + 2 * (b[i]+b[j])) % 2 == 0);
            map<ll, pii>::iterator it = pair_val.lower_bound(a_pair);
            if (it != pair_val.begin())
                it--;
            for (int k = 0; k < 2; ++k, ++it) {
                if (it == pair_val.end())
                    break;
                ll new_a_sum = a_sum - it->first + (b[i] + b[j]);
                ll new_b_sum = b_sum - (b[i] + b[j]) + it->first;
                if (ret_val > abs(new_a_sum - new_b_sum)) {
                    ret_val = abs(new_a_sum - new_b_sum);
                    ret.clear();
                    ret.push_back(pii(it->second.first, i));
                    ret.push_back(pii(it->second.second, j));
                }
            }
        }
    }
    cout << ret_val << endl;
    cout << ret.size() << endl;
    for (pii it: ret)
        cout << it.first+1 << " " << it.second+1 << endl;
    return 0;
}
