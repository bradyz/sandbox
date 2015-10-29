#include <iostream>
#include <vector>

using namespace std;

int N;

char grille[1001][1001];
char message[1001][1001];

void getMessage (vector<char>& result) {
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            if (grille[i][j] != '#')
                result.push_back(message[i][j]);
        }
    }
}

template <typename T>
void swp (T& a, T& b) {
    T tmp(a);
    a = b;
    b = tmp;
}

void rotate () {
    // transpose
    for (int i = 0; i < N / 2; ++i) {
        for (int j = i; j < N; ++j) {
            swp(grille[i][j], grille[j][i]);
        }
    }
    // swap columns
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N / 2; ++j) {
            swp(grille[i][j], grille[i][N-1-j]);
        }
    }
}

void print () {
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            cout << grille[i][j];
        }
        cout << endl;
    }
    cout << endl;
}

int main () {
    while (cin >> N && N) {
        vector<char> result;

        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                cin >> grille[i][j];
            }
        }

        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                cin >> message[i][j];
            }
        }

        getMessage(result); 

        rotate();
        getMessage(result); 

        rotate();
        getMessage(result); 

        rotate();
        getMessage(result); 

        for (auto it: result)
            cout << it;
        cout << endl;
    }
}
