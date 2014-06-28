import sys

def divby(n, a, b):
  result = False
  for x in range(a, b, 1):
    if(n % x == 0):
      result = True
      print "%d / %d == 0" % (n, x)
    else:
      result = False
      print "%d / %d != 0" % (n, x)
      break
  return result

x = 0
y = False
while(y == False):
  x += 20
  y = divby(x, 1, 20)

print x


