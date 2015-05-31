#include <iostream>
#include <vector>

using namespace std;

int main() {
    int a, b, tmp, idx = 0;
    int v[2000009];

    cin >> a;

    for(int i = 0; i < a; ++i) {
        cin >> tmp;
        for(int j = 0; j < tmp; ++j)
            v[++idx] = i + 1;
    }

    int t; 
    cin >> t;

    for(int i = 0; i < t; ++i) {
        cin >> tmp;
        cout << v[tmp] << endl;
    }

    return 0;
}
