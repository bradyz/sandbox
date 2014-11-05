#include <iostream>
#include <map>

int main () 
{
  int n;
  int k;
  int group_num;
  int count = 0; 
  std::map<int, int> group_list;

  //number inputs
  std::cin >> n; 

  for(k = 0; k < n; k++)
  {
    std::cin >> group_num;
    group_list[group_num] += 1;
  } 

  count += group_list[4];

  if(group_list[1] > 1 && group_list[3] > 1)
  {
    

  }


  std::cout << count << std::endl; 
  return 0;
}
