#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;

void add(int arr[], int N, int lo, int hi, int val)
{
    arr[lo] += val;
    if (hi != N - 1)
       arr[hi + 1] -= val;
}
 
//  Utility method to get actual array from operation array
void updateArray(int arr[], int N)
{
    //  convert array into prefix sum array
    for (int i = 1; i < N; i++)
        arr[i] += arr[i - 1];
}
 
//  method to print final updated array
void printArr(int arr[], int N)
{
    updateArray(arr, N);
    for (int i = 0; i < N; i++)
        cout << arr[i] << " ";
    cout << endl;
}

int main() {
  ios::sync_with_stdio(false);

  int N = (int) 1e6 + 5;
  int arr[N];

  for (int i = 0; i < N; i++)
    arr[i] = 0;

  int m, q;
  cin >> m >> q;

  for (int i = 0; i < m; i++) {
    int u, v;
    cin >> u >> v;

    //  Range add Queries
    add(arr, N, u, v-1, 1);
  }
  updateArray(arr, N);

  for (int i = 0; i < q; i++) {
    int t;
    cin >> t;

    cout << arr[t] << endl;
  }
  return 0;
}
