#include <iostream>
#include <unordered_set>

using namespace std;

int N;
unordered_set<int> values;

int gcd (int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

bool solve () {
    int prev;
    for (auto val: values) {
        if (prev && val != prev)
            return false;
        prev = val; 
    }
    return true;
}

int main () {
    cin >> N;
    int tmp;
    for (int i = 0; i < N; ++i) {
        cin >> tmp;
        while (tmp % 2 == 0 || tmp % 3 == 0) {
            if (tmp % 2 == 0)
                tmp /= 2;
            else
                tmp /= 3;
        }
        values.insert(tmp);
    }
    if (solve())
        cout << "Yes" << endl;
    else
        cout << "No" << endl;
    return 0;
} 
