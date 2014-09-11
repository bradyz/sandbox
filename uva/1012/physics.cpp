#include <iostream>

using namespace std;

int main() 
{
  int in0;
  int in1;
  int result;
  int index = 0;

  while(cin >> in0 >> in1)
  {
    result = in0 * 2 * in1;
    cout << result << "\n";
  }

  return 0;
}
