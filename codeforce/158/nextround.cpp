#include <iostream>

int main () 
{
  int n, k;
  int score, place, temp = 0;
  std::cin >> n >> k; 
  int count = n; 
  for(place = 1; place <= n; place++)
  {
    std::cin >> score;
    if(place == k)
      temp = score;

    if(score == 0 || ((temp > score) && (temp != 0)))
      count -= 1;
  } 
  std::cout << count << std::endl; 
  return 0;
}
