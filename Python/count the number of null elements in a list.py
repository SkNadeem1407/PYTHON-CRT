n=int(input("Enter the number of elements: "))
list=[]
count=0
for i in range(n):
    temp=int(input("Enter the elements: "))
    list.append(temp)
    for item in list:
        if item=="None":
            count+=1
print(count)


