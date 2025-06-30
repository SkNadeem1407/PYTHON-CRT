Leapyear=int(input("Enter the leap year: "))
if Leapyear%4==0 and Leapyear%100!=0:
    print("Valid leap year")
else:
    print("Invalid")