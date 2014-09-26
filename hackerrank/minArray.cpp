#include <iostream>
#include <vector>
#include <string>
#include <istream>

const int MAX_ARG = 100;

using namespace std;

int main()
{
  char buff[MAX_ARG];
  vector<int> myVector; 
  vector<int> myArgs;
  int firstLine = 1;
  int secondLine = 0;
  char *token;
  char *DELIM = " "; 

  getline(cin, buff);

  while(getline(cin, buff) != EOF)
  {
    if(firstLine) 
    {
      token = strtok(&buff[0], DELIM);
      while(token != NULL)
      {
        token = strtok(NULL, DELIM); 
      }

      myArgs[0] = atoi(&token[0]);
      myArgs[1] = atoi(&token[1]);

      firstLine = 0; 
      secondLine = 1;
    }
    else if(secondLine)
    {
      token = strtok(&buff[0], DELIM);
      while(token != NULL)
      {
        myVector.insert(myVector.begin(), atoi(token));
        token = strtok(NULL, DELIM); 
      }

      secondLine = 0;
    }
    else
    {
      token = strtok(&buff[0], DELIM);      
      while(token != NULL)
      {
        token = strtok(NULL, DELIM); 
      }
      int start = token[0]; 
      int end = token[1]; 
      int max = 0;
      int x;

      for(x = start; x <= end; x++)
      {
        if(max < myVector[x])
        {
          max = myVector[x];
        }
      }

      cout << max;
    }
  }

  return 0;
}
