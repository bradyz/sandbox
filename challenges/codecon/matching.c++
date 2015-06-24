#include <iostream>
#include <algorithm>
#include <string.h>
#include <vector>

using namespace std;

bool c[100000];
string d[100000];
int n, r;

int main() {
    memset(c, 1, sizeof(c));
    cin >> n;

    for(int i = 0; i < n; ++i)
        cin >> d[i];

    for(int i = 0; i < n; ++i) {
        if(d[i] == string(d[i].rbegin(), d[i].rend()))
            continue;

        for(int j = i + 1; j < n; ++j) {
            if(c[i] && c[j] && d[i] == string(d[j].rbegin(), d[j].rend())) {
                c[i] = c[j] = false;
                r += 1;
                break;
            }
        }

        if(c[i]) {
            r = -1;
            break;
        }
    }

    cout << r << endl;
}
