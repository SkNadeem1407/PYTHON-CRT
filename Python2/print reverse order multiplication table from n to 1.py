n=int(input("Enter the Value of n: "))
for i in range(n,0,-1):
    print(i)
    for j in range(10,0,-1):
        print(f"{i}x{j}={i*j}")
