#include <iostream>
#include <string>
#include <ctype.h>

//trying to do a one sweep, inplace implementation
//getting fancy with the iterators

using namespace std;

int main () 
{
  string in, result;
  bool convert = true;

  cin >> in; 
  string::iterator i;

  for(i = in.begin(); i != in.end(); i++)
  {
    if(i == in.begin())
    {
      convert = true;
      result += *i;
    }
    else if(i != in.begin() && convert && isupper(*i))
    {
      result += tolower(*i);
      convert = true;
    }
    else
      convert = false;
  }

  if(convert)
    cout << result << endl; 
  else
    cout << in << endl;

  return 0;
}
