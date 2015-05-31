#include <iostream>
#include <string>

using namespace std;

const string plus_sign = "++";
const string minus = "--";

int main () 
{
  int n, count;
  int x = 0;
  string input;
  cin >> n;
  for(count = 0; count < n; count++)
  {
    cin >> input;
    if(input.find(plus_sign) != string::npos)
      x += 1;
    else
      x -= 1;
  }

  cout << x << endl;
  
  return 0;
}
