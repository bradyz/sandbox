#include <vector>
#include <iostream>
#include "util.h"

using namespace std;

vector<int> myArr(10);

int main()
{
  int x;
  int count = 0;
  for(x = 0; x < myArr.size(); x++)
  {
    myArr[x] = count;
    count += 1;
  }

  for(x = 0; x < myArr.size(); x++)
  {
    cout << myArr[x] << "\n";
  }

  return 0;
}
