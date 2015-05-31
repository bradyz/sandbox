#include <iostream>
#include <string.h>
#include <stdio.h>
#include <cctype>

//trying to do a one sweep, inplace implementation
//getting fancy with the iterators


int main () 
{
  std::string a, b;
  std::string::iterator a_it, b_it;
  char *x, *y;
  int result = 0;

  std::cin >> a; 
  std::cin >> b; 

  a_it = a.begin();
  b_it = b.begin();

  while(b_it != b.end() && a_it != a.end())
  {
    *a_it = tolower(*a_it);
    *b_it = tolower(*b_it);
    a_it++;
    b_it++;
  }

  x = &a[0];
  y = &b[0]; 

  result = strcmp(x, y);

  if(result < 0)
    result = -1;
  else if(result > 0)
    result = 1;
  
  std::cout << result << std::endl;

  return 0;
}
