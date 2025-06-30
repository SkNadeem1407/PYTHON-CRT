'''
Sort a list of dates provided in DD-MM-YYYY format chronologically
Input:
An Integer n (1<n100)
A list of n strings in DD-MM-YYYY format
Output:
Sorted list of dates (earliest to latest)
Example:
Input["12-05-2023","01-01-2022","15-08-2021"]
Output["15-08-2021","01-01-2022","12-05-2023"]'''

arr=["12-05-2023","01-01-2022","15-08-2021"]
length=len(arr)
print(f"Original Array :{arr}")
for i in range(length-1):
  for j in range(length-i-1):
     d1 = arr[j].split('-')
     d2 = arr[j + 1].split('-')
     date1 = (int(d1[2]), int(d1[1]), int(d1[0]))
     date2 = (int(d2[2]), int(d2[1]), int(d2[0]))
     if date1 > date2:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]     
print("sorted array",arr)