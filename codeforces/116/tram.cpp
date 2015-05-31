#include <iostream>
#include <string>
#include <ctype.h>
#include <stdbool.h>

int main () 
{
  int n;
  int max = 0;
  int cur = 0;

  std::cin >> n;

  for(int x = 0; x < n; x++)
  {
    int a, b; 
    std::cin >> a >> b;

    cur -= a;
    cur += b;

    if(cur >= max)
      max = cur;
  }

  std::cout << max << std::endl;
  return 0;
}
