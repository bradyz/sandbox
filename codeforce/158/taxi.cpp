#include <iostream>
#include <map>

int main () 
{
  int n;
  int k;
  int group_num;
  int count = 0; 
  std::map<int, int> group_list;

  std::cin >> n;

  for(k = 0; k < n; k++)
  {
    std::cin >> group_num;
    group_list[group_num] += 1;
  }

  count += group_list[4];
  group_list[4] -= group_list[4];

  if(group_list[3] > 0)
  {
    if(group_list[1] > group_list[3])
    {
      //if there are more groups of 1 to pair with
      count += group_list[3];
      group_list[1] -= group_list[3];
      group_list[3] -= group_list[3];
    }
    else 
    {
      //there are less groups of 1
      group_list[3] -= group_list[1]; 
      count += group_list[1];
      group_list[1] -= group_list[1];
      count += group_list[3];
    }
  }

  if(group_list[2] > 0)
  {
    count += group_list[2] / 2;
    if(group_list[2] != 1)
      group_list[2] -= group_list[2] * 2;

    while(group_list[2] > 0 && group_list[1] > 0)
    {
      count += 1;
      group_list[2] -= group_list[1] * 2;  
      group_list[1] -= 2;
    }
    if(group_list[2] > 0)
      count += group_list[2];
  }

  if(group_list[1] > 0)
  {
    if(group_list[1] >= 4)
    {
      count += group_list[1] / 4;
      group_list[1] -= group_list[1] * 4;
    }
    if(group_list[1] > 0)
      count += 1;
  }

  std::cout << count << std::endl; 
  return 0;
}
