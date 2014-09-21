#include <iostream>
#include <vector>
#include <stdlib.h>

void printIntArray(std::vector<int> myArr)
{
  int x;
  
  for(x = 0; x < myArr.size(); x++)
  {
    std::cout << myArr[x] << " ";
  }

  std::cout << "\n";

}
