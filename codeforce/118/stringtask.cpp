#include <iostream>
#include <string>
#include <ctype.h>

int main () 
{
  const std::string STOP = "AaEeIiOoUu";
  std::string in;
  std::cin >> in; 
  std::string::iterator i = in.begin();
  while(i < in.end())
  {
    //std::cout << *i << std::endl;
    //std::cout << in << std::endl;
    if(STOP.find(*i) != std::string::npos)
    {
      in.erase(i);
    }
    else
    {
      if(isupper(*i))
        *i = tolower(*i);
      in.insert(i, '.');
      i += 2;
    }
  } 
  std::cout << in << std::endl; 
  return 0;
}
