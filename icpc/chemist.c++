#include <iostream>
#include <cstring>
#include <sstream>
#include <string>
#include <unordered_set>

using namespace std;

stringstream words("h he li be b c n o f ne na mg al si p s cl ar k ca sc ti v cr mn fe co ni cu zn ga ge as se br kr rb sr y zr nb mo tc ru rh pd ag cd in sn sb te i xe cs ba hf ta w re os ir pt au hg tl pb bi po at rn fr ra rf db sg bh hs mt ds rg cn fl lv la ce pr nd pm sm eu gd tb dy ho er tm yb lu ac th pa u  np pu am cm bk cf es fm md no lr");
int t;
string s;
unordered_set<string> w;
bool dp[50001];

int main () {
    while (words) {
        words >> s;
        w.insert(s);
    }

    cin >> t;

    for (int ct = 0; ct < t; ++ct) {
        memset(dp, false, sizeof(dp) * sizeof(bool));
        cin >> s;

        for (int i = 0; i < s.size(); ++i) {
            if (i == 0) {
                if (w.find(s.substr(i, 1)) != w.end())
                    dp[i] |= true;
                if (w.find(s.substr(i, 2)) != w.end())
                    dp[i+1] |= true;
            }
            else if (i == s.size()-1) {
                if (w.find(s.substr(i, 1)) != w.end() && dp[i-1])
                    dp[i] |= true;
            }
            else {
                if (w.find(s.substr(i, 1)) != w.end() && dp[i-1])
                    dp[i] |= true;
                if (w.find(s.substr(i, 2)) != w.end() && dp[i-1])
                    dp[i+1] |= true;
            }
        }

        if (dp[s.size()-1])
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }
}
