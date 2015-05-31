#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main () 
{
  int a, b;
  int tmp;
  int diff = 9999;
  vector<int> my_list;
  vector<int>::iterator it;
  cin >> a >> b;
  for(int x = 0; x < b; x++)
  {
    cin >> tmp;
    my_list.push_back(tmp);
  }

  sort(my_list.begin(), my_list.end());

  //for(it = my_list.begin(); it != my_list.end(); it++)
    //cout << *it << " ";

  //cout << endl;
  // 2 2
  // [1 2 3 4]
  it = my_list.begin();
  while(distance(it, my_list.end()) >= a)
  {
    tmp = *(it + a - 1) - *it;

    //cout << *(it + a - 1) << " - " << *it << " = " << tmp << endl;

    if(tmp < diff)
      diff = tmp; 

    it++;
  }

  cout << diff << endl;
  
  return 0;
}
