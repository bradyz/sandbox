#include <unordered_map>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    string c;
    string v;

    cin >> c;
    cin >> v;

    string l = c;
    transform(c.begin(), c.end(), l.begin(), ::tolower);
    unordered_map<char, int> match;

    vector<string> r;
    for(int i = 0; i < v.size(); ++i) {
        if(match.find(v[i]) == match.end())
            match[v[i]] = 1;
        else
            match[v[i]] += 1;
    }
    for(int i = 0; i < c.size()-v.size(); ++i) {
        unordered_map<char, int> tmp;

        for(int j = 0; j < v.size(); ++j) {
            if(tmp.find(l[i+j]) == tmp.end())
                tmp[l[i+j]] = 1;
            else
                tmp[l[i+j]] += 1;
        }

        if(tmp == match && c.substr(i, v.size()) != v) {
            r.push_back(c.substr(i, v.size()));
        }
    }

    sort(r.begin(), r.end());

    for(int i = 0; i < r.size(); ++i) {
        cout << r[i] << endl;
    }
}
