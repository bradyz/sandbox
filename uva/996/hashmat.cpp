#include <iostream>
#include <sstream>

using namespace std;

int main ()
{
  string input;
  char* arr;
  int in0;
  int in1;

  while(getline(cin, input))
  {
    in0 = atoi(input[0]);
    in1 = atoi(input[1]);

    printf("%d", in0);

  }

  return 0;
}
