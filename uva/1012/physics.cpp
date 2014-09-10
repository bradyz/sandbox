#include <iostream>

using namespace std;

int main() 
{
  int in0;
  int in1;
  int result;
  int output[10];
  int index = 0;

  while(cin >> in0 >> in1)
  {
    output[index] = in0 * 2 * in1;
    index += 1;
  }

  for(int x = 0; x < index; x++)
  {
    cout << output[x] << "\n";
  }

  return 0;
}
