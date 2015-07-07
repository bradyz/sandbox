#include <iostream>

using namespace std;

int n, s, t;
int c[101];
bool u[101];

int main() {
    cin >> n;
    s = n;

    for(int i = 0; i < n; ++i) {
        u[i] = false;
        cin >> c[n-i-1];
    }

    while(s > 0) {
        if(c[s-1] < s && !u[s-1-c[s-1]]) {
            u[c[s-1]] = true;
            t = c[s-1];
            c[s-1] = c[s-c[s-1]-1];
            c[s-t-1] = t;
        }
        else {
            cout << c[s-1];
            s -= 1;
            if(s != 0) 
                cout << ",";
        }
    }

    cout << endl;
}
