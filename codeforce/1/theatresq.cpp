#include <iostream>
#include <cmath>
#include <vector>

int main () 
{
  int length, width;
  int area;
  int result;

  std::cin >> length >> width >> area;

  result = (length * width) / area;

  std::cout << result << std::endl; 

  return 0;
}
