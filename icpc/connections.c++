#include <iostream>
#include <vector>
#include <unordered_set>
#include <algorithm>

using namespace std;

int T;
int N, M;
bool a[1000001];
vector<int> b;
int total;

int main () {
    ios_base::sync_with_stdio(false);
    cin >> T;
    int tmp;
    int aMin = 1000001;
    int bMin = 1000001;
    int aMax = -1;
    int bMax = -1;
    for (int i = 0; i < T; ++i) {
        cin >> N >> M;
        unordered_set<int> sums;
        for (int j = 0; j < N; ++j) {
            cin >> tmp;;
            a[tmp] = true;
            aMin = min(aMin, tmp);
            aMax = max(aMax, tmp);
        }
        for (int j = 0; j < M; ++j) {
            cin >> tmp;
            b.push_back(tmp);
            bMin = min(bMin, tmp);
            bMax = max(bMax, tmp);
        }
        for (int j = aMin+bMin; j <= aMax+bMax; ++j) {
            for (int k = 0; k < b.size(); ++k) {
                if (j - b[k] < 100001 && j - b[k] > 0 && a[j-b[k]]) {
                    total += 1;
                    break;
                }
            }
        }
        cout << total << endl;
    }
    return 0;
}
