#include <iostream>
#include <sstream>

using namespace std;

int probtres( int n ) 
{
  
  int count = 1;

  while ( n != 1 ) {
    if (n % 2 == 1) {
      n = 3 * n + 1;
    } 
    else {
      n = n / 2;
    }

    count++; 
  }

  return count;
}

int main () 
{
  //first number
  int input1;
  //second number
  int input2;
  int arr[100];
  int index = 0;
  string input;
  int max;

  while (getline(cin, input)) {
    istringstream is(input);
    is >> input1;
    is >> input2;

    if (input1 > input2)
    {
      arr[index + 1] = input1;
      arr[index] = input2;
    }
    else
    {
      arr[index] = input1;
      arr[index + 1] = input2;
    }

    index += 2;
  }

  for(int y = 0; y < index - 1; y += 2)
  {
    max = 0;
     
    for(int x = arr[y]; x <= arr[y+1]; x++) 
    {
      int temp = probtres(x);
      if (temp > max)
        max = temp;
    }

    cout << arr[y] << " " << arr[y+1] << " " << max << "\n";
  }

  return 0;
}
