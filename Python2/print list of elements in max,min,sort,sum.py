'''''''''''
n=int(input("Enter the size of List: "))
Num=[]
for i in range(n):
    Temp=int(input(f"Enter the element at{i} index:"))
    Num.append(Temp)
print(f"Given List: {Num}")
print("maximum element :",max(Num))
print("minimum element :",min(Num))
print("summation :",sum(Num))
print("maximum element :",sorted(Num))'''''''''
#list of cartoons
cartoons=['Ben10','Phines & Ferb','Kid vs cat','Jackie chan']
print(cartoons)
print("After Appending : ")
cartoons.append('Roll no 21')
print(cartoons)
cartoons.insert(0,'scoobydoo')
print(cartoons)
cartoons.pop(0)
print(cartoons)
cartoons.remove('Phines & Ferb')
print(cartoons)
cartoons.index('Ben10')
print(cartoons)
cartoons.reverse()
print(cartoons)

