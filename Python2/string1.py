str="python"
print(f"length of {str} is {len(str)}")
#accessing without index
for i in str:
    print(i,end=" ")
print()
#accessing with index
for i in range(len(str)):
    print(str[i],end=" ")