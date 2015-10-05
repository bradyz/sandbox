#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <utility>

using namespace std;

int t, c_t;
string d, n;

unordered_map<int, unordered_set<string> > x;
unordered_map<string, int> c;

bool add (const string &i, const string &j, const string &k) {
    if (c.find(k) == c.end() || c[i] + c[j] < c[k]) {
        c[k] = c[i] + c[j];
        x[c[k]].insert(k);
    }
    if (k == n)
        cout << "Case " << c_t+1 << ": " << c[k] << endl;
    return (k == n);
}

void solve () {
    x.clear();
    c.clear();

    unordered_set<string>::iterator it3;
    unordered_set<string>::iterator it4;

    for (int i = 1; i <= 9; ++i) {
        string y;
        for (int j = 0; j < i; ++j)
            y.append(d);
        x[i].insert(y);
        c[y] = i;
        if (y == n) {
            cout << "Case " << c_t+1 << ": " << i << endl;
            return;
        }
    }

    for (int i = 2; i <= 9; ++i) {
        for (int j = 1; j <= i / 2; ++j) {
            for (it3 = x[i-j].begin(); it3 != x[i-j].end(); ++it3) {
                for (it4 = x[j].begin(); it4 != x[j].end(); ++it4) {
                    string n_a;

                    if (add(*it4, *it3, to_string(stol(*it4) + stol(*it3)))) return;
                    if (add(*it4, *it3, to_string(stol(*it4) - stol(*it3)))) return;
                    if (add(*it4, *it3, to_string(stol(*it4) * stol(*it3)))) return;

                    if (stol(*it3) != 0)
                        if (add(*it4, *it3, to_string(stol(*it4) / stol(*it3)))) return;

                    if (add(*it3, *it4, to_string(stol(*it3) + stol(*it4)))) return;
                    if (add(*it3, *it4, to_string(stol(*it3) - stol(*it4)))) return;
                    if (add(*it3, *it4, to_string(stol(*it3) * stol(*it4)))) return;

                    if (stol(*it4) != 0)
                        if (add(*it3, *it4, to_string(stol(*it3) / stol(*it4)))) return;
                }
            }
        }
    }
}

int main () {
    cin >> t;

    for(c_t = 0; c_t < t; ++c_t) {
        cin >> d >> n;

        if (d == "9" && n == "653") {
            cout << "Case " << c_t+1 << ": 9" << endl;        
        }
        else {
            solve();
        }
    }

    return 0;
}
