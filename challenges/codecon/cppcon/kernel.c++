#include <iostream>
#include <algorithm>
#include <sstream>
#include <vector>
#include <string>
#include <set>

using namespace std;

int main() {
    vector<set<string> > v;
    string t, x;

    set<string> blah;
    v.push_back(blah);

    int count = 0;
    bool endwithkernel = false;

    while(getline(cin, x)) {
        stringstream s(x);

        while(s >> t) {
            for(size_t i = 0; i < t.length(); ++i) {
                if(isalpha(t[i]))
                    continue;
                t[i] = ' ';
            }

            stringstream s_b(t);
            string new_t;

            while(s_b >> new_t) {
                transform(new_t.begin(), new_t.end(), new_t.begin(), ::tolower);
                if (new_t.find("kernel") == string::npos) {
                    count += 1;
                    set<string> blah; 
                    v.push_back(blah);
                    endwithkernel = true;
                }
                else {
                    v.back().insert(new_t);
                    endwithkernel = false;
                }
            }
        }
    }

    int r = 0;

    for(int i = 0; i < v.size(); ++i)
        r += v[i].size();

    if(!endwithkernel)
        r -= v.back().size();

    cout << r / count << endl;
}
