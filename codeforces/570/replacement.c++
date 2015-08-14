#include <iostream>

char c[300000];
int n, m;
int x, z;
char y;

using namespace std;

int main () {
    cin >> n >> m;

    for(int i = 0; i < n; ++i) {
        cin >> c[i];
        if(c[i] == c[i-1] && c[i] == '.') 
            z += 1;
    }

    for(int i = 0; i < m; ++i) {
        cin >> x >> y;
        x -= 1;

        if(y == '.' && c[x] != '.') {
            if(x-1 >= 0 && c[x-1] == '.')
                z += 1;
            if(x+1 < n && c[x+1] == '.')
                z += 1;
        }
        else if(y != '.' && c[x] == '.') {
            if(x-1 >= 0 && c[x-1] == '.')
                z -= 1;
            if(x+1 < n && c[x+1] == '.')
                z -= 1;
        }

        cout << z << endl;
        c[x] = y;
    }
}
