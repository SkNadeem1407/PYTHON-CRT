str1=input("Enter the first sequence:")
str2=input("Enter the second sequence:")
if len(str1)==len(str2):
    print("Both sequences are in same length: ")
else:
    print("Not in same length: ")
differences=[i+1 for i in range(len(str1))if str1[1]!=str2[2]]
print("Sequences differ at positions:", differences)
else:
print




