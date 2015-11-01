#include <iostream>
#include <algorithm>

using namespace std;

int T;
int K;
int times[1000001];

int binarysearch (int val) {
    int lo = 0; 
    int hi = K-1;
    while (lo+1 < hi) {
        int mi = (lo+hi) / 2;
        if (times[mi] > val)
            hi = mi; 
        else
            lo = mi;
    }
    return hi;
}

int main () {
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cin >> K;
        for (int k = 0; k < K; ++k)
            cin >> times[k];
        int notes = 0;
        for (int i = 0; i < K; ++i)
            notes = max(notes, i - binarysearch(times[i]-5000) + 1);
        cout << "Case " << t << ": " << K + notes << endl;
    }
    return 0;
}
