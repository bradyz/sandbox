import sys
import math

number = int(sys.argv[1])

def isPrime(n):
  prime = True
  for i in range(2, n/2, 1):
    if(n % i == 0):
      prime = False
      break
  return prime

def factors(n):
  f = [1]
  for i in range(2, n, 1):
    if(n % i == 0):
        f.append(i)
  return f

def prime_factor(n):
  big = 1
  a = factors(n)
  for x in a:
    if isPrime(x):
      big = x
  return x

def better_way(n):
  prime = True
  num = 1
  for i in range(1, n/int(math.floor(math.sqrt(n))), 1):
    if(isPrime(i) & (n % i == 0)):
      num = i
      n = n/i
      print "num - %d\t n - %d" % (num, n)
  return num

print(better_way(number))
