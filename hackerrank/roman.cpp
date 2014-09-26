#include <iostream>
#include <vector>
#include <string>
#include <istream>
#include <map>

const int MAX_ARG = 100;

using namespace std;



int main()
{
  map<int a, string b> romanValues;
  int keys[15];
  romandValues[1000] = "M";
  keys[0] = 1000;
  romandValues[900] = "D";
  keys[1] = 900;
  romandValues[500] = "CD";
  keys[2] = 500;
  romandValues[400] = "C";
  keys[3] = 400;
  romandValues[100] = "C";
  keys[4] = 100;
  romandValues[90] = "XC";
  keys[5] = 90;
  romandValues[50] = "L";
  keys[6] = 50;
  romandValues[40] = "XL";
  keys[7] = 40;
  romandValues[10] = "X";
  keys[8] = 10;
  romandValues[9] = "IX";
  keys[9] = 9;
  romandValues[5] = "V";
  keys[10] = 5;
  romandValues[4] = "IV";
  keys[11] = 4;
  romandValues[1] = "I";
  keys[12] = 1;
  romandValues[0] = NULL;
  keys[13] = NULL;


  while(el >= romanValues[index])
  {
    result += romandValues[index];
    el -= keys[index];
  }
  

}
