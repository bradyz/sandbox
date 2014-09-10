#include <iostream>
#include <cmath> 

using namespace std;

int main ()
{
  double in0;
  double in1;
  double dif;
  int index = 0;
  double output[10];

  while(cin >> in0 >> in1)
  {
    if (in0 > in1)
      dif = in0 - in1;
    else
      dif = in1 - in0; 
    output[index] = dif; 
    index += 1;
  }

  for(int x = 0; x < index; x++) 
  {
    printf("%.0f\n", output[x]);
  }

  return 1;
}
