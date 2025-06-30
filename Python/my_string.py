input=input("Enter the String: ")
char=list(input)
print("List of Characters:",char)
for i in input:
    print(i,end="")
print()
length= len(input)
print("length of the string: ",length)
min_char=min(char)
print("Minimum character in the string: ",min_char)
space=0
for char in input:
    if char==' ':
     space+=1
print("Number of spaces present in the string: ",space)


