#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void swap(int* a, int* b) {
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

void permutations(vector<int> arr, int l, int r, vector<vector<int> >& perm) {
    if (l == r+1) {
        vector<int> tmp(arr);
        perm.push_back(tmp);
        return;
    }
    for (int i = l; i <= r; ++i) {
        swap(arr[l], arr[i]);
        permutations(arr, l+1, r, perm);
        swap(arr[l], arr[i]);
    }
}

int main () {
    int arr[] = {5, 6, 7};
    vector<vector<int> > perm;
    vector<int> val(arr, arr+sizeof(arr)/sizeof(arr[0]));

    permutations(val, 0, 2, perm);

    for (auto it: perm) { 
        cout << it[0] << " " << it[1] << " " << it[2] << endl;
    }

    cout << endl;

    do {
        cout << arr[0] << " " << arr[1] << " " << arr[2] << endl;
    }
    while (next_permutation(arr, arr+sizeof(arr)/sizeof(int)));

    return 0;
}
