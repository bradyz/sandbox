#include <unordered_set>
#include <unordered_map>
#include <iostream>
#include <string>
#include <queue>
#include <utility>

using namespace std;

class Solution {
    public:
        bool is_close (const string& a, const string& b) {
            if (a.size() != b.size())
                return false;

            int diff = 0;

            for (int i = 0; i < a.size(); ++i) {
                if (a[i] != b[i])
                    diff += 1;
            }

            return diff == 1;
        }

        unordered_map<string, unordered_set<string> > graph (const string& b, const string& e, unordered_set<string> w) {
            w.insert(b);
            w.insert(e);

            unordered_map<string, unordered_set<string> > g;
            unordered_set<string>::iterator it1, it2;

            for (it1 = w.begin(); it1 != w.end(); ++it1) {
                for (it2 = it1; it2 != w.end(); ++it2) {
                    if (it2 == it1)
                        ++it2;

                    if (it2 == w.end())
                        break;

                    if (is_close(*it1, *it2)) {
                        g[*it1].insert(*it2); 
                        g[*it2].insert(*it1); 
                    }
                    
                }
            }

            return g;
        }

        int path_length(string& b, string& e, unordered_map<string, string>& p) {
            string cur = e;
            int len = 0;

            cout << cur << endl;

            while (cur != b) {
                cur = p[cur];
                len += 1;
                cout << cur << endl;
            }
            
            return len+1;
        }

        int ladderLength(string b, string e, unordered_set<string>& w) {
            unordered_map<string, unordered_set<string> > g = graph(b, e, w);
            unordered_map<string, string> p;

            queue<string> q;

            unordered_set<string>::iterator it;

            string cur;

            p[b] = "";
            q.push(b);

            while (!q.empty()) {
                cur = q.front(); 
                q.pop();

                if (cur == e)
                    return path_length(b, e, p);

                for (it = g[cur].begin(); it != g[cur].end(); ++it) {
                    if (p.find(*it) != p.end())
                        continue;

                    p[*it] = cur;
                    q.push(*it);
                }
            }

            return 0;
        }
};

int main () {
    string start;
    string end;
    string tmp;

    unordered_set<string> dict;

    cin >> start;
    cin >> end;

    while (cin >> tmp) {
        dict.insert(tmp);
    }

    Solution s;    
    cout << s.ladderLength(start, end, dict) << endl;
}
