N=int(input("Enter the value of n: "))
def sum_n(N):
    return N*(N+1)//2
temp=sum_n(N)
print(f"Sum of first {N} natural numbers is {temp}")
