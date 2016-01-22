#include <cstdio>
#include <vector>
#include <algorithm>
#include <utility>
#include <unordered_map>

using namespace std;

typedef pair<int, int> pii;

int N;
int pearls[300005];

bool sort_func (pii a, pii b) {
    if (a.second < b.second)
        return true;
    return false;
}

int main () {
    scanf("%d", &N);
    unordered_map<int, int> idx;
    vector<pii> intervals;
    for (int i = 1; i <= N; ++i) {
        scanf("%d", &pearls[i]);
        if (idx.find(pearls[i]) != idx.end())
            intervals.push_back(pii(idx[pearls[i]], i));
        idx[pearls[i]] = i;
    }
    sort(intervals.begin(), intervals.end(), sort_func);
    if (intervals.size() == 0) {
        printf("-1\n");
    }
    else {
        vector<pii> result;
        result.push_back(intervals.front());
        result.front().first = 1;
        for (auto it: intervals) {
            if (it.first <= result.back().second)
                continue;
            result.push_back(pii(result.back().second+1, it.second));
        }
        result.back().second = N;
        printf("%d\n", result.size());
        for (auto it: result)
            printf("%d %d\n", it.first, it.second);
    }
    return 0;
}
