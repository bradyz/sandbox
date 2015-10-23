#include <iostream>
#include <vector>

using namespace std;

int main () {
    int c[] = {1, 2, -3, 4, -1, 2, -6};

    int maxSoFar = 0;
    vector<int> maxSoFarArray;
    int maxEndingHere = 0;
    vector<int> maxEndingHereArray;

    for (int i = 0; i < sizeof(c)/sizeof(int); ++i) {
        maxEndingHere += c[i];
        maxEndingHereArray.push_back(c[i]);

        if (maxEndingHere <= 0) {
            maxEndingHere = 0;
            maxEndingHereArray.clear();
        }
        else if (maxEndingHere > maxSoFar) {
            maxSoFar = maxEndingHere;
            maxSoFarArray = maxEndingHereArray;
        }
    }

    for (auto it: maxSoFarArray)
        cout << it << " ";
    cout << endl;

    return 0;
}
