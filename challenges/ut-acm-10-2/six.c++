#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <utility>
#include <set>

using namespace std;

int t;
int c_t;
string d;
string n;

unordered_map<int, unordered_set<string> > x;
unordered_map<string, int> c;

struct Node {
    string a;

    Node (string x="") : a(x) {}

    bool operator< (const Node& rhs) const {
        return (c[this->a] > c[rhs.a]); 
    }
};

void solve () {
    x.clear();
    c.clear();

    priority_queue<Node> q;

    unordered_map<int, unordered_set<string> >::iterator it1;
    unordered_set<string>::iterator it3;
    set<pair<string, string> > vis;

    Node a;

    for (int i = 1; i <= 9; ++i) {
        string y;
        for (int j = 0; j < i; ++j)
            y.append(d);
        x[i].insert(y);
        c[y] = i;
        q.push(Node(y));
    }

    while (q.size() > 0) {
        a = q.top();
        q.pop();
        
        if (a.a == n) {
            cout << "Case " << c_t+1 << ": " << c[a.a] << endl;
            return;
        }

        for (int i = 1; i <= 9; ++i) {
            if (c[a.a] + i > 9)
                break;

            for (it3 = x[i].begin(); it3 != x[i].end(); ++it3) {
                if (vis.find(pair<string, string>(a.a, *it3)) != vis.end() 
                        || vis.find(pair<string, string>(*it3, a.a)) != vis.end())
                    continue;

                vis.insert(pair<string, string>(a.a, *it3));
                vis.insert(pair<string, string>(*it3, a.a));

                string n_a = to_string(stol(a.a) + stol(*it3));
                
                if (c.find(n_a) == c.end() || c[a.a] + i < c[n_a]) {
                    c[n_a] = c[a.a] + i;
                    x[c[n_a]].insert(n_a);
                    q.push(Node(n_a));
                }

                n_a = to_string(stol(a.a) - stol(*it3));

                if (c.find(n_a) == c.end() || c[a.a] + i < c[n_a]) {
                    c[n_a] = c[a.a] + i;
                    x[c[n_a]].insert(n_a);
                    q.push(Node(n_a));
                }

                n_a = to_string(stol(a.a) * stol(*it3));

                if (c.find(n_a) == c.end() || c[a.a] + i < c[n_a]) {
                    c[n_a] = c[a.a] + i;
                    x[c[n_a]].insert(n_a);
                    q.push(Node(n_a));
                }

                if (stol(*it3) == 0)
                    continue; 

                n_a = to_string(stol(a.a) / stol(*it3));

                if (c.find(n_a) == c.end() || c[a.a] + i < c[n_a]) {
                    c[n_a] = c[a.a] + i;
                    x[c[n_a]].insert(n_a);
                    q.push(Node(n_a));
                }
            }
        }
    }
}

int main () {
    cin >> t;

    for(c_t = 0; c_t < t; ++c_t) {
        cin >> d >> n;
        solve();
    }

    return 0;
}
