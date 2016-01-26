#include <cstdio>
#include <vector>
#include <unordered_map>

using namespace std;

int N;
vector<int> result;
unordered_map<int, int> last;

int main () {
    result.push_back(0);
    scanf("%d", &N);
    for (int i = 1; i <= N; ++i) {
        int tmp;
        scanf("%d", &tmp);
        if (last.find(tmp) != last.end()) {
            result.push_back(i);
            last.clear();
        }
        else
            last[tmp] = i;
    }
    if (result.size() == 1) {
        printf("-1\n");
    }
    else {
        printf("%ld\n", result.size()-1);
        for (int i = 1; i < result.size(); ++i) {
            if (i == result.size()-1)
                printf("%d %d\n", result[i-1]+1, N);
            else
                printf("%d %d\n", result[i-1]+1, result[i]);
        }
    }
    return 0;
}
