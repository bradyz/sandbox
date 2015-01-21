#include <iostream>

using namespace std;

int main(int argc, char **argv) {

  string s;

  while(getline(cin, s)) {
    if(s == "42")
      break;
    cout << s << endl;
  }
}
