n=int(input("Enter the number of elements: "))
list=[]
for i in range(n):
    temp=int(input("Enter the elements: "))
    list.append(temp)
if n>=2:
    list[0],list[-1]=list[-1],list[0]
    print("swapping first and last elements: ",list)