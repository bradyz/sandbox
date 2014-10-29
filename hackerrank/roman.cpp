#include <iostream>
#include <vector>
#include <string>
#include <istream>
#include <map>

using namespace std;

int main()
{
  map<int, string> romanValues;
  int keys[15];
  romanValues[1000] = "M";
  keys[0] = 1000;
  romanValues[900] = "D";
  keys[1] = 900;
  romanValues[500] = "CD";
  keys[2] = 500;
  romanValues[400] = "C";
  keys[3] = 400;
  romanValues[100] = "C";
  keys[4] = 100;
  romanValues[90] = "XC";
  keys[5] = 90;
  romanValues[50] = "L";
  keys[6] = 50;
  romanValues[40] = "XL";
  keys[7] = 40;
  romanValues[10] = "X";
  keys[8] = 10;
  romanValues[9] = "IX";
  keys[9] = 9;
  romanValues[5] = "V";
  keys[10] = 5;
  romanValues[4] = "IV";
  keys[11] = 4;
  romanValues[1] = "I";
  keys[12] = 1;
  romanValues[0] = "\0";
  keys[13] = NULL;

  int el = 0;
  string result = "";
  int index = 0;

  while(el >= keys[index])
  {
    result += romanValues[index];
    el -= keys[index];
  } 
}
