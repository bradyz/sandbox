# Stock Max
# Dynamic Programming
# 12:11 AM Oct - 8

def maxprice(myArr, num):
  return 0

numCases = int(input())

for x in range(0, numCases):
  numArgs = int(input())
  stockArr = [int(y) for y in input().split()]
  print(maxPrice(stockArr, numArgs))
