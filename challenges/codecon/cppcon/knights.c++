#include <iostream>
#include <algorithm>

using namespace std;

int c[3];
int n, m, r;
bool cont;

int main() {
    for(int i = 0; i < 3; ++i) {
        cin >> c[i];
    }

    cin >> n;

    cont = true;

    while(cont) {
        m = 0;

        for(int i = 0; i < 3; ++i) {
            if(c[i] < c[m]) {
                m = i;
            }
        }

        if(m == 0) {
            if(c[1] - n <= 0 || c[2] - n <= 0) {
                r += min(c[1], c[2]);
                cont = false;
            }
            c[1] -= n;
            c[2] -= n;
        }
        if(m == 1) {
            if(c[0] - n <= 0 || c[2] - n <= 0) {
                r += min(c[0], c[2]);
                cont = false;
            }
            c[0] -= n;
            c[2] -= n;
        }
        if(m == 2) {
            if(c[0] - n <= 0 || c[1] - n <= 0) {
                r += min(c[0], c[1]);
                cont = false;
            }
            c[0] -= n;
            c[1] -= n;
        }

        if(cont)
            r += n;
    }

    cout << r << endl;
}
