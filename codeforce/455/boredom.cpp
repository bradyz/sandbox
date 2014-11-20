#include <map>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main () {
  int a;
  int tmp;
  int count = 0;
  int max = 0;
  vector<int> my_vect;

  cin >> a;

  for(int x = 0; x < a; x++) {
    cin >> tmp;
    my_vect.push_back(tmp);
  }

  //because of the push_backs
  reverse(my_vect.begin(), my_vect.end());

  int *it;

  //count is the position of the piece to remove
  while(count < a)
  {
    //tmp sum
    tmp = 0;
    it = &my_vect[0];

    while(it <= &my_vect[my_vect.size() - 1])
    {
      if(it != &my_vect[count - 1] && it != &my_vect[count + 1])
        tmp += *it;

      it++;
    }

    if(tmp > max) max = tmp;
    count++;
  }


  cout << max << endl;

  return 0;
}
