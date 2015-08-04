#include <iostream>
#include <string>
#include <algorithm>

using namespace std; 

int main() {
    string n, m;
    cin >> n;
    cin >> m;

    int dif = 0;

    for(int i = 0; i < min(n.size(), m.size()); ++i) {
        if(n[i] != m[i]) {
            dif += 1;
        }
    }

    if(m.size() != n.size()) {
        dif += 1;
    }

    if(dif > 1) {
        cout << "FALSE" << endl;
    }
    else {
        cout << "TRUE" << endl;
    }
}
