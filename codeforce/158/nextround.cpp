#include <iostream>

int main () 
{
  int n, k;
  int score, temp;
  int place;
  int count = 0;

  std::cin >> n >> k;

  for(place = 1; place <= n; place++)
  {
    std::cin >> score;
    if(place == k)
      temp = score;

    if(score < temp || score == 0)
    {
      std::cout << count << std::endl;
      return 0;
    } 

    count++;
  }

  std::cout << count << std::endl;

  return 0;
}
