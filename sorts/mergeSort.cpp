#include <vector>
#include <iostream>
#include <stdlib.h>
#include "util.h"

std::vector<int> myArr(10);

std::vector<int> merge(std::vector<int> leftArr, std::vector<int> rightArr) 
{
  std::vector<int> result;

  printIntArray(leftArr);
  printIntArray(rightArr);

  int left = 0;
  int right = 0;
  int x;

  for(x = 0; x < ((int) leftArr.size() + (int) rightArr.size()); x++)
  {
    if((right >= ((int) rightArr.size())) || ((left <= ((int) leftArr.size() - 1) && (leftArr[left] <= rightArr[right]))))
    {
      result.push_back(leftArr[left]);
      left++;
    }
    else
    {
      result.push_back(rightArr[right]);
      right++;
    }
    printIntArray(result);
  }

  return result;
}

std::vector<int> mergeSort(std::vector<int> unsortedArray, int left, int right)
{
  int center = (left + right) / 2;

  if(left < right)
  {
    std::vector<int> leftArray = mergeSort(unsortedArray, left, center); 
    std::vector<int> rightArray = mergeSort(unsortedArray, center + 1, right);

    return merge(leftArray, rightArray);
  }

  std::vector<int> resultVector(1); 
  resultVector[0] = unsortedArray[left];

  return resultVector;
}

int main()
{
  int x;
  int y;
  int tmp;

  myArr = randomArray(20, 20);

  printIntArray(myArr);

  std::vector<int> result = mergeSort(myArr, 0, myArr.size() - 1);

  printIntArray(result);

  return 0;
}
