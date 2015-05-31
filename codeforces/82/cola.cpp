#include <string>
#include <iostream>

using namespace std;

const string a = "Sheldon";
const string b = "Leonard";
const string c = "Penny";
const string d = "Rajesh";
const string e = "Howard";

int main () 
{
  int n;
  int x = 1;
  string name[] = {a, b, c, d, e};

  cin >> n;

  while(x * 5 < n)
  {
    n -= x * 5;
    x *= 2;
  }

  cout << name[(n - 1) / x] << endl;

  return 0;
}
