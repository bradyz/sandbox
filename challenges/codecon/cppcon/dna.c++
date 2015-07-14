#include <iostream>
#include <string>

using namespace std;

int main() {
    string n, t;
    string r;
    int m = 0;
    cin >> n;
    int x = n.size();

    for(int i = 0; i < n.size(); i += 3) {
        for(int j = 3; i+j+j <= n.size(); j += 3) {
            string y = n.substr(i, j);
            for(int k = i+j; k <= n.size(); k += 3) {
                string z = n.substr(k, j);

                if(y == z && j > m) {
                    m = j;
                    r = y;
                }
            }
        }
    }

    cout << r << endl;
}
