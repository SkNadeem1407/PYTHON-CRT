Num=int(input("Enter the Integer value: "))
if(Num>0):
     print(f"{Num}is +ve Number")
elif(Num<0):
     print(f"{Num}is -ve Number")
else:
     print(f"{Num}is 0")
Res="+ve Num" if(Num>0) else"-ve Number"
print(f"{Res}")