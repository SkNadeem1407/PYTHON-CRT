'''''''''''
n=int(input("Enter the size of list: "))
Prog_lang=[]
for i in range(n):
    Temp=input("Enter a programming lang: ")
    Prog_lang.append(Temp)
print("Elements of the list: ")
print(Prog_lang)'''''''''
#deleteing of list
color=['white','black','blue','red','brown']
print(color)
del color[2]
print(color)
del color
print(color)