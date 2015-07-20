#include <iostream>
#include <string>
#include <stdlib.h>
#include <cstring>
#include <cstdlib>

using namespace std;

char* toString(int n, int m)
{
    char digits[] = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
    int i;
    char buf[66];   /* enough space for any 64-bit in base 2 */

    buf[65] = '\0';
    i = 65;

    if (n > 0){
        while (n){
            buf[--i] = digits[n % m];
            n /= m;
        }
    }
    else{
        while(n){
            buf[--i] = digits[-(n % m)];
            n /= m;
        }
        buf[--i] = '-';
    }   

    return strdup(buf + i);
}

int main() {
    int n, m;
    cin >> n;
    cin >> m;

    cout << toString(n, m) << endl;
}
