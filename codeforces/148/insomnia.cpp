#include <iostream>
#include <stdio.h>
#include <vector>

using namespace std;

int main () 
{
  int tmp;
  int count = 0;
  vector<int> my_arr;

  cin >> tmp;
  my_arr.push_back(tmp);
  cin >> tmp;
  my_arr.push_back(tmp);
  cin >> tmp;
  my_arr.push_back(tmp);
  cin >> tmp;
  my_arr.push_back(tmp);

  cin >> tmp;

  while(tmp > 0)
  {
    for(int i = 0; i < (int) my_arr.size(); i++)
    {
      if(tmp % my_arr[i] == 0)
      {
        count += 1;
        break;
      }
    }

    tmp -= 1;
  }

  std::cout << count << std::endl;

  return 0;
}
