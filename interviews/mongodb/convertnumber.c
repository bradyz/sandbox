#include <string.h>
#include <stdlib.h>
#include <stdio.h>

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

int main(int argc, char **argv)
{
  FILE *fr;
  char buf[20];
  int n = 0;
  int index = 0;

  fr = fopen("convertnumber-input.txt", "rt");

  // first line of the file
  fgets(buf, 20, fr);
  n = atoi(buf);

  // number of inputs
  int arr[n]; 

  for(index = 0; index < n; index++)
  {
    int tmp;

    // each line contains another input
    if(fgets(buf, 20, fr) != NULL)
    {
      tmp = atoi(buf);
      arr[index] = tmp;
    }
  }

  // safely close the file
  fclose(fr);

  for(index = 0; index < n; index++)
  {
    char *tmp = NULL;
    itos(&tmp, arr[index]);

    if(tmp != NULL)
    {
      printf("Int: %d ", arr[index]);
      printf("Str: '%s'\n", tmp); 
    }

    free(tmp);
  }

  return 0;
}
