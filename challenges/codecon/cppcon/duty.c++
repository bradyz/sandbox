#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <set>

using namespace std;

int main() {
    vector<string> c;
    string t, x;

    while(getline(cin, x)) {
        stringstream s(x);
        set<string> y;

        while(s >> t) {
            c.push_back(t);
        }
    }

    for(int i = 0; i < c.size(); ++i) {
        cout << c[i] << endl;
    }
}
