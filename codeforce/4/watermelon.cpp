#include <iostream>
#include <string>

int main () 
{
  int weight;
  std::string result = "NO";

  std::cin >> weight;

  if(weight != 2)
    result = ((weight % 2) == 1) ? "NO" : "YES";

  std::cout << result << std::endl; 

  return 0;
}
