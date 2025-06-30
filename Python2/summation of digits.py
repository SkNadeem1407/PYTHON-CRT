n=int(input("Enter the value of n: "))
Temp=n
digit_sum=0
Rem=0
while(n!=0):
    Rem=n%10
    digit_sum=digit_sum+Rem
    n=n//10
print(f"Summation is {digit_sum} ")