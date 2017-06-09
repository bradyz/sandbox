#include <iostream>
#include <algorithm>
#include <set>
#include <map>

using namespace std;

typedef long long ll;

int n;
ll prices[200005];
set<ll> values;
map<ll, ll> counts;

int main () {
  cin >> n;

  for (int i = 0; i < n; i++) {
    cin >> prices[i];

    values.insert(prices[i]);
    counts[prices[i]]++;
  }

  ll best = 1e18;

  for (int i = 0; i < n; i++) {
    counts[prices[i]]--;

    if (counts[prices[i]] == 0)
      values.erase(prices[i]);

    if (values.size() == 0)
      break;

    ll val = *--(values.lower_bound(prices[i]));

    if (val >= prices[i])
      continue;

    best = min(best, prices[i] - val);
  }

  return 0;
}
