#include <map>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main () {
  int a;
  int tmp;
  int x = 0;
  int max = 0;
  map<int, int> my_map;

  cin >> a;

  for(int x = 0; x < a; x++) {
    cin >> tmp;
    my_map[tmp] += 1;
  }

  map<int, int>::iterator it;
  map<int, int>::iterator it2;

  for(it = my_map.begin(); it != my_map.end(); it++)
  {
    tmp = 0;
    it2 = my_map.begin();
    x = it->first;
    while(it2 != my_map.end())
    {
      if(it2->first + 1 != x && it2->first - 1 != x)
        tmp += it2->first * it2->second;
      
      it2++;
    }
    if(tmp > max) 
      max = tmp;
  }

  cout << max << endl;

  return 0;
}
