#prime numbers from 1 to n
N=int(input("Enter the value of n: "))
def prime_num(num):
    count=0
    for i in range(1,num+1):
        if(num%i==0):
            count+=1
    if count==2:
        print(f"{num}")
for i in range(1,N+1):
    prime_num(i)


#prime numbers from n to 1
N = int(input("Enter the value of n: "))
def prime_num(num):
    count=0
    for i in range(1,num+1):
        if (num%i==0):
            count+=1
    if count==2:
        print(f"{num}")
for i in range(N,0,-1):
    prime_num(i)

