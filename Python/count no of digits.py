n=int(input("Enter the value of n: "))
Temp=n
digit_count=0
while(n!=0):
    n=n//10
    digit_count+=1
print(f"{Temp} has {digit_count} digits")