#include <iostream>
#include <queue>
#include <string>
#include <cstring>

using namespace std;

#define MAX_N 100001

int T;
int K;
bool p[MAX_N];
vector<int> vp;

void primes () {
    memset(p, true, sizeof(p));
    p[0] = false;
    p[1] = false;
    for (int i = 2; i < MAX_N; ++i) {
        if (!p[i])
            continue;
        vp.push_back(i);
        for (int j = i + i; j < MAX_N; j += i)
            p[j] = false;
    }
    for (int i = 0; i < vp.size(); ++i)
        cout << vp[i] << endl;
}

bool check (string k) {
    for (int i = 0; i < k.size(); ++i) {
        if (k[i] != '0' && k[i] != '1') 
            return false;
    }
    return true;
}

int main () {
    // cin >> T;
    primes();
    T = 0;
    for (int t = 0; t < T; ++t) {
        cin >> K;
        cout << check(to_string(K)) << endl;
        int found = -1;
        priority_queue<int, vector<int>, less<int> > pqueue;
        pqueue.push(K);
        while (pqueue.size() > 0 && found == -1) {
            int cur = pqueue.top();
            pqueue.pop();
            cout << cur << endl;
            if (check(to_string(cur)))
                found = cur;
            pqueue.push(cur * 3);
            pqueue.push(cur * 7);
        }
        cout << found << endl;
    }
    return 0;
}
