#include <map>
#include <fstream>
#include <iostream>
#include <string.h>
#include <stdlib.h>

const int MAX_CHAR = 512;
const int MAX_TOKENS = 10;
const char* DELIMITER = " ";

int main()
{
  std::map <std::string, int> myMap;
  std::ifstream myFile;
  std::ofstream outFile;

  myFile.open("inputCount.txt");

  while(!myFile.eof())
  {
    char buf[MAX_CHAR];
    myFile.getline(buf, MAX_CHAR);

    int n = 0;
    char* parsed[MAX_TOKENS] = {};
    parsed[0] = strtok(buf, DELIMITER);

    while(parsed[n] != NULL)
    {
      myMap[parsed[n]] += 1;
      std::cout << parsed[n] << myMap[parsed[n]] << "\n";
      n++;
      parsed[n] = strtok(NULL, DELIMITER);
    }
  }

  outFile.open("outputCount.txt");

  for(auto &kv : myMap)
  {
    outFile << kv.first << " " << kv.second << "\n";  
  }

  return 0;
}
