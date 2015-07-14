#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int t;
    int m = 0;
    vector<int> c;

    while(cin >> t) {
        c.push_back(t);
    }

    for(int i = 0; i < c.size(); ++i) {
        for(int j = i+1; j < c.size(); ++j) {
            m = max(m, c[j]-c[i]);
        }
    }

    cout << m << endl;
}
