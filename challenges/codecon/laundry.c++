#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <unordered_map>

using namespace std;

int main() {
    vector<string> c;
    unordered_map<string, int> v;
    string t;

    while(getline(cin, t)) {
        if(t != "")
            c.push_back(t);
    }

    for(int i = 0; i < c.size(); ++i) {
        if(v.find(c[i]) == v.end())
            v[c[i]] = 1;
        else
            v[c[i]] += 1;
    }


    sort(c.begin(), c.end());

    for(int i = 0; i < c.size(); ++i) {
        if(c[i].find("sock") != string::npos) {
            if(v[c[i]] > 1) 
                cout << v[c[i]] / 2 << "|" << c[i] << endl;
            if(v[c[i]] % 2 == 1) 
                cout << 0 << "|" << c[i] << endl;
        }
        else
            cout << v[c[i]] << "|" << c[i] << endl;
        i += v[c[i]] - 1;
    }
}
