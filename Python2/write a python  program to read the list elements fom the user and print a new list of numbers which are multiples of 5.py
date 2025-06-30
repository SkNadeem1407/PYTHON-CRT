from zstandard.backend_cffi import new_nonzero

n=int(input("Enter the size of list: "))
list=[]
for i in range(n):
    Temp=int(input("Enter the number : "))
    list.append(Temp)
print("Elements of the list: ")
new_list=[]
for i in list:
    if (i % 5 == 0):
        new_list.append(i)
print(new_list)
