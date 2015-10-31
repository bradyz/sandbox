#include <iostream>
#include <string>

using namespace std;

int main () {
    int n;
    string word;
    cin >> n;

    for (int i = 0; i < n; ++i) {
        cin >> word;
        if (word == "Dropbox")
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }
}
