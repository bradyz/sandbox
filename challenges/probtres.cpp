#include <iostream>

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

    std::cout << count << " " << n;
    count++; 
  }

  return count;
}

int main () 
{
  int input1;
  int input2;
  int max;

  std::cin >> input1 >> input2;

  max = probtres(input1);

  for( ; input1 <= input2; ++input1) {
    int tmp = probtres(input1);
    std::cout << tmp << "\n";
    if (tmp > max) {
      max = tmp;
    }
  }

  std::cout << max << "\n";
}
