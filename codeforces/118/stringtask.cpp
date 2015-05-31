#include <iostream>
#include <string>
#include <ctype.h>

//trying to do a one sweep, inplace implementation
//getting fancy with the iterators

int main () 
{
  std::string STOP = "AaEeIiOoUuYy";
  std::string in, result;
  std::cin >> in; 
  std::string::iterator i = in.begin();
  while(i < in.end())
  {
    if(STOP.find(*i) == std::string::npos)
    {
      result.append(1, '.');
      result.append(1, tolower(*i));
    }
    i++;
  } 
  std::cout << result << std::endl; 
  return 0;
}
