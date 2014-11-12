#include <iostream>
#include <string>

using namespace std;

const string plus_sign = "++";
const string minus = "--";

int main () 
{
  int n;
  int count = 0;
  string input;
  string::iterator it;

  cin >> n;
  cin >> input;
  it = input.begin();
  while(it != input.end())
  {
    if(*it == *(it + 1))
    {
      input.erase(it + 1);
      count += 1;
      it = input.begin();
    }
    else 
      it += 1;
  }

  cout << count << endl;
  
  return 0;
}
