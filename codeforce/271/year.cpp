#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main () 
{
  bool cont = true;
  int in;
  int arr[4] = {};
  int result = 0;

  vector<int> myVector;
  vector<int>::iterator it;
  

  cin >> in;
  
  in += 1;

  //1934
  while(cont)
  {
    arr[0] = in / 1000 % 10;
    arr[1] = in / 100 % 10;
    arr[2] = in / 10 % 10;
    arr[3] = in % 10;
    myVector = vector<int>(arr, arr + 4);

    sort(myVector.begin(), myVector.begin() + 4);

    it = myVector.begin();

    while(it < myVector.end() - 1)
    {
      if(*it == *(it + 1))
        break;
      else
      {
        if(it == myVector.end() - 2)
        {
          cont = false;
          result = in;
          break;
        }
      }

      it += 1;
    }

    in += 1;
  }
  
  cout << result << endl;
  
  return 0;
}
