#include <iostream>
#include <cstring>
#include <vector>

using namespace std;

bool c[100000000];
int n;
vector<int> r;

int main() {
    memset(c, 0, sizeof(c));
    cin >> n;

    for(int i = 1; i <= n; ++i) {
        for(int j = i; j <= n; j += i) {
            c[j] = !c[j];
        }
    }

    for(int i = 1; i <= n; ++i) {
        if(c[i]) {
            r.push_back(i);
        }
    }

    for(int i = 0; i < r.size(); ++i) {
        cout << r[i];
        if(i != r.size()-1) {
            cout << ",";
        }
    }

    cout << endl;
}
