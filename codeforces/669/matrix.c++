#include <iostream>

using namespace std;

int mat[105][105];
int n, m, q;
int a;
int x, y, v;
int qt[10005][4];

void shift_row (int a) {
  int tmp = mat[a][m-1];
  for (int i = m-1; i > 0; --i)
    mat[a][i] = mat[a][i-1];
  mat[a][0] = tmp;
}

void shift_col (int a) {
  int tmp = mat[n-1][a];
  for (int i = n-1; i > 0; --i)
    mat[i][a] = mat[i-1][a];
  mat[0][a] = tmp;
}

int main () {
  cin >> n >> m >> q;

  for (int i = 0; i < q; ++i) {
    cin >> qt[i][0];
    if (qt[i][0] == 1) {
      cin >> a;
      qt[i][1] = a-1;
    }
    else if (qt[i][0] == 2) {
      cin >> a;
      qt[i][1] = a-1;
    }
    else if (qt[i][0] == 3) {
      cin >> x >> y >> v;
      qt[i][1] = x-1;
      qt[i][2] = y-1;
      qt[i][3] = v;
    }
  }

  for (int i = q-1; i >= 0; --i) {
    if (qt[i][0] == 1)
      shift_row(qt[i][1]);
    else if (qt[i][0] == 2)
      shift_col(qt[i][1]);
    else if (qt[i][0] == 3)
      mat[qt[i][1]][qt[i][2]] = qt[i][3];
  }

  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < m; ++j)
      cout << mat[i][j] << " ";
    cout << endl;
  }

  return 0;
}
