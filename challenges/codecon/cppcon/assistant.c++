#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    string x;
    string t;
    vector<string> c;
    vector<int> v;
    int b, e;

    getline(cin, x);

    for(int i = 0; i < x.size(); ++i) {
        if(x[i] == '[') {
            v.push_back(i+2);
        }
        else if(x[i] == ']' && v.size() > 0) {
            e = i-2;
            b = v.back();
            c.push_back(x.substr(b, e-b+1));
            v.pop_back();
        }
    }

    for(int i = 0; i < c.size(); ++i) {
        cout << c[i] << endl;
    }

    return 0;
}
