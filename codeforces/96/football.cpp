#include <iostream>
#include <string>

using namespace std;

int main () 
{
  int count = 1;
  string input;
  string::iterator it;

  cin >> input;

  for(it = input.begin(); it != input.end() - 1; it++)
  {
    if(*it == *(it + 1))
    {
      count++;
      if(count >= 7)
      {
        cout << "YES" << endl;
        return 0;
      }
    }
    else
      count = 1;
  }

  cout << "NO" << endl; 
  return 0;
}
