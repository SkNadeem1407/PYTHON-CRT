Month=int(input("Enter the Month Number: "))
if Month in [4,6,9,11]:
    print("30 days")
elif Month in [1,3,5,7,8,10,12]:
    print("31 days")
elif Month==2:
    print("28 or 29 days")
else:
    print("Invalid")


