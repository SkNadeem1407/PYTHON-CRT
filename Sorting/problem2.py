'''1. Sort Student Scores Problem: You are given an array of integers representing student scores. Your task is to sort the array in ascending order using a basic sorting algorithm (Buble Sort / Selection Sort / Insertion Sort).
Input:
An integer n (1 < n < 1000) - number of students An array of n integers - the scores (0 < score < 100) Output:
Sorted array of scores in ascending order
Input: 5
Scores: [(55, 90,70, 60, 80] Output: [55,60,70,80,90]
'''

arr=[55, 90,70, 60, 80]
length=len(arr)
print(f"Original Array :{arr}")
for i in range(length-1):
  for j in range(length-i-1):
    if (arr[j]>arr[j+1]):
      temp=arr[j]
      arr[j]=arr[j+1]
      arr[j+1]=temp
print("sorted array",arr)