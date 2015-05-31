#include <iostream>
#include <cmath>
#include <vector>

int main () 
{
  long double length, width;
  long double side;
  long double result;

  std::cout.precision(22);
  std::cin >> length >> width >> side;

  result = std::ceil(length/side) * std::ceil(width/side);

  std::cout << result << std::endl; 

  return 0;
}
