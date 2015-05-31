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
  int n;
  int count = 0;

  std::cin >> n;

  for(int x = 0; x < n; x++)
  {
    int a, b, c; 
    std::cin >> a >> b >> c;

    if((a + b + c) >= 2)
      count += 1;
  }

  std::cout << count << std::endl;
  return 0;
}
