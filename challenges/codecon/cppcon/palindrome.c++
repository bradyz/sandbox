#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    string t;
    int m = 0;
    
    cin >> t;

    for(int i = 0; i < t.size(); ++i) {
        for(int k = t.size()-1; k > i; --k) {
            int x = 0;
            int j = 0;
            while(i+j <= k-j) {
                if(t[i+j] == t[k-j]) {
                    if(i+j == k-j)
                        x += (t[i+j] - '@');
                    else
                        x += 2 * (t[i+j] - '@');
                    j += 1; 
                }
                else {
                    x = -1;
                    break;
                }
            }
            m = max(m, x);
        }
    }

    cout << m << endl;
}
