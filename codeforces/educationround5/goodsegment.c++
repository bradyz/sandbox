#include <cstdio>
#include <unordered_map>

using namespace std;

int N, K;
int a[1000005];

int main () {
    scanf("%d %d", &N, &K);
    for (int i = 0; i < N; ++i)
        scanf("%d", a + i);
    int x = 0, y = 0;
    int i = 0, j = 0;;
    int cur = 0;
    unordered_map<int, int> occur;
    while (i < N && j < N) {
        if (cur <= K) {
            if (occur.find(a[j]) == occur.end() || occur[a[j]] == 0) {
                occur[a[j]] = 1;
                ++cur;
            }
            else
                ++occur[a[j]];
            if (cur <= K && (j - i) > (y - x)) {
                x = i;
                y = j;
            }
            ++j;
        }
        else {
            --occur[a[i]];
            if (occur[a[i]] == 0)
                --cur;
            ++i;
        }
    }
    printf("%d %d\n", x+1, y+1);
    return 0;
}
