#include <string.h>
#include <stdlib.h>
#include <stdio.h>

FILE *fr;

int num_digits(int input) 
{
  int digits = 1;
  int counter = 0;
  while(input / digits > 0)
  {
    digits *= 10;
    counter++;
  }
  return counter;
}

void itos(char **dest, int input) 
{
  int size = num_digits(input);
  int counter = 0;
  int digits = 1;
  char *output1 = (char *) malloc(size * sizeof(char));
  while(input / digits > 0)
  {
    char tmp = '0' + input / digits % 10;
    memcpy(output1 + size - counter - 1, &tmp, sizeof(tmp));
    counter++;
    digits *= 10;
  }

  *dest = output1;
}

int main ()
{
  char buf[20];
  int n = 0;
  int index = 0;

  fr = fopen("convertnumber-input.txt", "rt");
  fgets(buf, 20, fr);
  n = atoi(buf);
  int arr[n]; 

  for(index = 0; index < n; index++)
  {
    int tmp;

    if(fgets(buf, 20, fr) != NULL)
    {
      tmp = atoi(buf);
      arr[index] = tmp;
    }
  }

  for(index = 0; index < n; index++)
  {
    char *tmp = NULL;
    itos(&tmp, arr[index]);

    if(tmp != NULL)
    {
      printf("Int: %d\n", arr[index]);
      printf("Str: %s\n", tmp); 
    }
  }

  return 0;
}
