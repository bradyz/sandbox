#include <iostream>
#include <sstream>
#include <map>
#include <string>
#include <set>

using namespace std;

int main() {
   map<string, int> c; 
   string t, x;

   while(getline(cin, x)) {
       stringstream s(x);
       set<string> y;

       while(s >> t) {
           if(y.find(t) == y.end()) {
               if(c.find(t) == c.end())
                   c[t] = 1;
               else
                   c[t] += 1;
               y.insert(t);
           }
       }
   }

   for(map<string, int>::iterator it = c.begin(); it != c.end(); ++it) {
       if(it->second == 1) 
           cout << it->first << endl;
    }
}
