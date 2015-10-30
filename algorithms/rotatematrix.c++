#include <iostream>

using namespace std;

int n = 5;
int A[5][5] = {{1, 2, 3, 4, 5},
               {6, 7, 8, 9, 10},
               {11, 12, 13, 14, 15},
               {16, 17, 18, 19, 20},
               {21, 22, 23, 24, 25}};

void CWrotate () {
    for (int i = 0; i <= (n-1)/2; i++) {
        for (int j = i; j < n-i-1; j++) {
            int tmp = A[i][j];
            A[i][j] = A[n-j-1][i];
            A[n-j-1][i] = A[n-i-1][n-j-1];
            A[n-i-1][n-j-1] = A[j][n-i-1];
            A[j][n-i-1] = tmp;
        }
    }
}

void CCWrotate () {
    for (int i = 0; i < n / 2; i++) {
        for (int j = i; j < n-i-1; j++) {
            int tmp = A[i][j];
            A[i][j] = A[j][n-i-1];
            A[j][n-i-1] = A[n-i-1][n-j-1];
            A[n-i-1][n-j-1] = A[n-j-1][i];
            A[n-j-1][i] = tmp;
        }
    }
}

void print () {
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j)
            cout << A[i][j] << "\t";
        cout << endl;
    }
    cout << endl;
}

int main () {
    print();

    CWrotate();
    print();
    
    CCWrotate();
    print();


    return 0;
}
