#include <iostream>
#include <string>

using namespace std;

void end (void)
{
  cout << "YES" << endl;
}

int main () 
{
  string in;
  char a = 'H';
  char b = 'Q';
  char c = '9';

  cin >> in;
  
  if(in.find(a) != string::npos)
    end();
  else if(in.find(b) != string::npos)
    end();
  else if(in.find(c) != string::npos)
    end();
  else
    cout << "NO" << endl;
  
  return 0;
}
