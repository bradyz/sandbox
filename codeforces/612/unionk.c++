#include <cstdio>
#include <vector>
#include <algorithm>
#include <utility>

using namespace std;

typedef pair<int, int> ii;
typedef vector<ii> vii;

int N, K;

bool eventSort (ii lhs, ii rhs) {
    if (lhs.first < rhs.first)
        return true;
    else if (lhs.first == rhs.first and lhs.second > rhs.second)
        return true;
    return false;
}

int main () {
    scanf("%d %d", &N, &K);
    vii events;
    for (int i = 0; i < N; ++i) {
        int a, b;
        scanf("%d %d", &a, &b);
        events.push_back(ii(a, 1));
        events.push_back(ii(b, -1));
    }
    sort(events.begin(), events.end(), eventSort);
    vii result;
    int cur = 0;
    int start;
    bool flag = false;
    for (ii event: events) {
        cur += event.second;
        if (!flag && cur >= K) {
            flag = true;
            start = event.first;
        }
        else if (flag && cur == K-1) {
            flag = false;
            result.push_back(ii(start, event.first));
        }
    }
    printf("%d\n", result.size());
    for (ii event: result)
        printf("%d %d\n", event.first, event.second);
    return 0;
}
