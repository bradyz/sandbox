#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

int readInt(int low, int high){
  int x;

  if(scanf("%d", &x) != 1){
    fprintf(stderr, "Haven't found input");
    throw;
  }

  if(!(low <= x && x <= high)){
    fprintf(stderr, "Expected int in range [%d, %d], but found %d!", low, high, x);
    throw;
  }

  return x;
}

int main(){
  int num_input = readInt(1, 10);

  for(int Ti = 0; Ti < num_input; Ti++) {
    int arr_size = readInt(1, 100000);
    vector<int> a(arr_size);

    for(int i = 0; i < arr_size; i++)
      a[i] = readInt(1, 20000);

    vector<long long> x(arr_size);

    for(int i = 0; i < arr_size; i++) {
      x[i] = (i == 0 ? 0 : x[i - 1]) + a[i];
    }

    long long sum = 0;
    int cnt = 0;

    for(int i = arr_size - 1; i >= 0; --i) {
      long long left = (i == 0 ? 0 : x[i - 1]);
      if(left == sum)
        cnt++;
      sum += a[i];
    }

    puts(cnt == 0 ? "NO" : "YES");
  }

  return 0;
}
