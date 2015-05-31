#include <iostream>
#include <string>
#include <ctype.h>
#include <stdbool.h>

bool even(int n)
{
  if(n % 2 == 0)
    return true;
  return false;
}

int main () 
{
  int x, y;
  int answer;
  int count = 0;
  std::cin >> x >> y;
  std::cin >> answer;

  count += x * y / 2;

  if(count == answer)
    std::cout << "PASS: " << count << "\n";
  else
    std::cout << "FAIL: " << count << "\n";

  return 0;
}
