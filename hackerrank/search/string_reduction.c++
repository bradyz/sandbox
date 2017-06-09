#include <iostream>
#include <string>
#include <map>

using namespace std;

int n;
map<string, int> memo;

int solve(string query) {
  if (memo.find(query) != memo.end())
    return memo[query];

  int result = query.size();

  for (int i = 1; i < query.size(); i++) {
    if (query[i] == query[i-1])
      continue;

    string left = query.substr(0, i-1);
    string right = query.substr(i+1);
    string mid;

    bool has_a = (query[i] == 'a' || query[i-1] == 'a');
    bool has_b = (query[i] == 'b' || query[i-1] == 'b');
    bool has_c = (query[i] == 'c' || query[i-1] == 'c');

    if (has_a && has_b)
      mid = "c";
    else if (has_a && has_c)
      mid = "b";
    else if (has_b && has_c)
      mid = "a";

    result = min(result, solve(left + mid + right));
  }

  return (memo[query] = result);
}

int main () {
  cin >> n;

  for (int i = 0; i < n; i++) {
    string query;
    cin >> query;

    cout << solve(query) << endl;
  }

  return 0;
}
