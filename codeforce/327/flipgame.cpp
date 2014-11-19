#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int flip_add (int x, int y, vector<int> c) {
  int sum = 0;
  
  for(int a = x; a <= y; a++) {
    if(c[a] == 0)
      c[a] = 1;
    else
      c[a] = 0;
  }

  for(vector<int>::iterator it = c.begin(); it != c.end(); it++)
    sum += *it;

  return sum;
}

int main () {
  int a;
  int tmp;
  int max = 0;
  vector<int> my_vect;

  cin >> a;

  for(int x = 0; x < a; x++) {
    cin >> tmp;
    my_vect.push_back(tmp);
  }

  reverse(my_vect.begin(), my_vect.end());

  for(int x = 0; x < a; x++) {
    for(int y = x; y < a; y++) {
      vector<int> copy_vect;
      copy_vect = my_vect;
      tmp = flip_add(x, y, copy_vect);

      if(tmp > max) 
        max = tmp;
    }
  }

  cout << max << endl;

  return 0;
}
