#include <iostream>
#include <map>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

string c[10001];

int main() {
    int n;
    map<map<char, int>, int> v;
    map<map<char, int>, vector<int> > r;

    cin >> n;

    for(int i = 0; i < n; ++i) {
        int asdf;
        cin >> asdf;
        string t = to_string(asdf);
        c[i] = t;
        map<char, int> tmp;

        for(int j = 0; j < c[i].size(); ++j) {
            if (t[j] == '0')
                continue;
            if (tmp.find(c[i][j]) == tmp.end())
                tmp[c[i][j]] = 1;
            else
                tmp[c[i][j]] += 1;
        }

        if(v.find(tmp) == v.end())
           v[tmp] = 1; 
        else
           v[tmp] += 1; 

        r[tmp].push_back(asdf);
    }

    int m = 0;
    map<char, int> i;

    for(map<map<char, int>, int>::iterator it = v.begin(); it != v.end(); ++it) {
        if (it->second > m) {
            m = it->second;
            i = it->first;
        }
    }

    sort(r[i].begin(), r[i].end());

    cout << r[i].size() << " ";
    for(int j = 0; j < r[i].size(); ++j) {
        cout << r[i][j] << endl;
        break;
    }
}
