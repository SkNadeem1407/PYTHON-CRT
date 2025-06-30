N=int(input("Enter the value of n: "))
def Factorial(N):
    if N<0:
        return
    elif N==0 or N==1:
        return 1
    else:
        return N*Factorial(N-1)
print(f"Factorial of {N} is {Factorial(N)}")

