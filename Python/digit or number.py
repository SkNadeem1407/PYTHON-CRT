Num=int(input("Enter the Integer Value: "))
if(Num>=-9 and Num<=9):
    print(f"{Num}is Digit")
else:
    print(f"{Num}is Number")
Result="Digit" if(Num>=9 and Num<=9)else"Number"
print(f"{Num} is {Result}")