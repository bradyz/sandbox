#include <string>
#include <iostream>

int main()
{
  std::string a = "asdf";
  std::string b = "";
  int x = 0;

  char *end = &a[a.length() - 1];

  for(x = a.length() - 1; x >= 0; x--)
  {
    b.push_back(*end);
    end--;
  }

  std::cout << b << "\n";

  return 0;
}
