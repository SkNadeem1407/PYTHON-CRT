Arr=[25,20,15,10,5]
print(f"Original Array : {Arr}")
for i in range(len(Arr)):
    flag=False
    for j in range(len(Arr)-1):
        if Arr[j]>Arr[j+1]:
            Arr[j],Arr[j+1]=Arr[j+1],Arr[j]
            print(Arr)
            flag=True
    if flag==False:
        break
print(Arr)