n=int(input("Enter the Value of n: "))
for i in range(1,n+1):
    print(i)
    for j in range(10,0,-1):
        print(f"{i}x{j}={i*j}")
