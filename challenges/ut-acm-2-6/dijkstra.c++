#include <iostream>
#include <unordered_map>
#include <map>


using namespace std;

int t; 
int k, n;
int a[1000000];

int main () {
    cin >> t;
    while (t--) {
        cin >> k >> n;
        multimap<int, int> pqueue;
        unordered_map<int, int> c;
        for (int i = 0; i < n; ++i)
            cin >> a[i];
        for (int i = 0; i < k; ++i) {
            if (c.find(a[i]) != c.end())
                c[a[i]] += 1;
            else
                c[a[i]] = 1;
            pqueue.insert(multimap<int, int>::value_type(a[i], 1));
        }
        cout << pqueue.begin()->first << " ";
        for (int i = k; i < n; ++i) {
            c[a[i-k]] -= 1;
            c[a[i]] += 1;
            pqueue.insert(multimap<int, int>::value_type(a[i], 1));
            int tmp = pqueue.begin()->first;
            while (c[tmp] <= 0) {
                pqueue.erase(pqueue.begin());
                tmp = pqueue.begin()->first;
            }
            pqueue.insert(multimap<int, int>::value_type(tmp, 1));
            cout << tmp << " ";
        }
        cout << endl;
    }
    return 0;
}
