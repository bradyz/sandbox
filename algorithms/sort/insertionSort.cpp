#include <vector>
#include <iostream>
#include <stdlib.h>
#include "util.h"

std::vector<int> myArr(10);

int main()
{
  int x;
  int y;
  int tmp;
  int steps = 0;

  myArr = randomArray(10, 10);

  printIntArray(myArr);

  for(x = 1; x < myArr.size(); x++)
  {
    tmp = myArr[x];
    for(y = x; y > 0 && tmp < myArr[y - 1]; y--)
    {
      myArr[y] = myArr[y - 1];
      printIntArray(myArr);
    }
    myArr[y] = tmp;
    printIntArray(myArr);
  }


  return 0;
}
