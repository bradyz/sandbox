#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

static void find_min(int x, int y);

int* my_arr;

int main(int argc, char** argv)
{
  int n = 0;
  int min = 999;
  int a, b, c, d;
  int as, bs, cs, ds;
  int arr[] = {9, 9, 3, 9, 8, 6, 1, 5, 5, 7, 5, 8};

  my_arr = (int *) malloc(n * sizeof(int));
  my_arr = arr;

  n = 12;

  //if(argc == 1)
    //n = atoi(argv[1]);

  a = fork();
  if(a == 0)
    find_min(0, n / 4);
  else
  {
    b = fork();
    if(b == 0)
      find_min(n / 4, n / 2);
    else
    {
      c = fork();
      if(c == 0)
        find_min(n /2, 3 * n /4);
      else
      {
        d = fork();
        if(d == 0)
          find_min(3 * n / 4, n);
        else
        {
          waitpid(a, &as, 0);
          waitpid(b, &bs, 0);
          waitpid(c, &cs, 0);
          waitpid(d, &ds, 0);

          if(WEXITSTATUS(as) < min)
            min = WEXITSTATUS(as);
          
          if(WEXITSTATUS(bs) < min)
            min = WEXITSTATUS(bs);

          if(WEXITSTATUS(cs) < min)
            min = WEXITSTATUS(cs);

          if(WEXITSTATUS(ds) < min)
            min = WEXITSTATUS(ds);

          printf("Min is %d \n", min);
        }
      }
    }
  }


  exit(0);
}

static void find_min(int x, int y)
{
  int min = 999;
  int n;

  for(n = x; n < y; n++)
  {
    if(my_arr[n] < min)
      min = my_arr[n];
  }

  exit(min);
  return;
}
