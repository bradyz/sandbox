#include <iostream>
#include <unordered_map>
#include <cstring>
#include <algorithm>

using namespace std;

int N;
int values[100001];
int sorted[100001];

int main () {
    cin >> N;
    for (int n = 0; n < N; ++n)
        cin >> values[n];
    memcpy(sorted, values, N * sizeof(int));
    sort(sorted, sorted+N);
    // for (int i = 0; i < N; ++i)
    //     cout << values[i] << " ";
    // cout << endl;
    // for (int i = 0; i < N; ++i)
    //     cout << sorted[i] << " ";
    // cout << endl;
    int res = 0;
    for (int i = 0; i < N;) {
        unordered_map<int, int> missing;
        for (int j = i; j < N; ++j) {
            // cout << "i: " << i << " j:" << j << endl;
            if (missing.find(sorted[j]) != missing.end()) {
                missing[sorted[j]] += 1;
                if (missing[sorted[j]] == 0)
                    missing.erase(sorted[j]);
            }
            else
                missing[sorted[j]] = 1;
            if (missing.find(values[j]) != missing.end()) {
                missing[values[j]] -= 1;
                if (missing[values[j]] == 0)
                    missing.erase(values[j]);
            }
            else 
                missing[values[j]] = -1;
            // for (auto it: missing)
            //     cout << it.first << " " << it.second << endl;
            // cout << endl;
            if (missing.size() == 0) {
                // cout << "res: " << res << endl;
                ++res;
                i = j+1;
                break;
            }
        }
    }
    cout << res << endl;
}
