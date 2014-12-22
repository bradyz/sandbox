#include <string.h>
#include <stdlib.h>
#include <stdio.h>

int main ()
{
  int input = 10;
  int digits = 1;
  int counter = 0;

  while(input / digits > 0)
  {
    digits *= 10;
    counter++;
  }

  printf("Counter: %d\n", counter);

  char *output1 = (char *) malloc(counter * sizeof(char));
  char *output2 = (char *) malloc(counter * sizeof(char));

  output1[counter - 1] = '\0';
  int size = strlen(output1);
  int sizof = sizeof(output1);
  printf("Malloc: %d \n", counter * sizeof(char));
  printf("Size: %d \n", size);
  printf("Sizeof: %d \n", sizof);

  char tmp;

  counter = 0;
  digits = 1;

  while(input / digits > 0)
  {
    tmp = '0' + input / digits % 10;
    memcpy(output1 - counter, &tmp, sizeof(tmp));
    counter++;
    digits *= 10;
  }

  //reverse the string

  printf("output1: %s\n", output1);

  sprintf(output2, "%d", input);
  printf("output2: %s\n", output2);

  return 0;
}
