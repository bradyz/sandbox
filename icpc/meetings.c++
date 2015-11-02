#include <iostream>
#include <algorithm>

using namespace std;

int T;
int N, M;
int number[100001];
int allowed[100001];

int main () {
    cin >> T;
    for (int t = 0; t < T; ++t) {
        cin >> N >> M;
        for (int i = 0; i < N; ++i)
            cin >> number[i];
        for (int i = 0; i < M; ++i)
            cin >> allowed[i];
        sort(number, number+N);
        sort(allowed, allowed+M);
        int i = 0;
        int j = 0;
        int result = 0;
        while (i < N && j < M) {
            if (number[i] <= allowed[j]) {
                result += 1;
                i += 1;
            }
            j += 1;
        }
        cout << result << endl;
    }
    return 0;
}
