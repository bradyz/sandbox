#include <string>
#include <iostream>

std::string smush(std::string n)
{
  int count = 0;
  for(std::string::iterator i = n.begin() + 1; i < n.end() - 1; ++i)
  {
    count += 1;
  }

  std::string result = "";
  //std::string result = n.at(0) + std::to_string(count) + n.at(n.size() - 1);

  return result; 
}

int main () 
{
  int num;
  int x;

  std::cin >> num;

  for(x = 0; x < num; x++)
  {
    std::string to_smush = "";
    std::cin >> to_smush; 
    if(to_smush.size() <= 10)
      std::cout << to_smush << std::endl;
    else
    {
      int len = to_smush.length();
      std::cout << to_smush.at(0) << len - 2 << to_smush.at(len - 1) << std::endl;
    }
  }

  return 0;
}
