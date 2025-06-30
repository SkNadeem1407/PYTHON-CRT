Str="NADEEM"
for i in range(len(Str)):
    for j in range(len(Str)):
        print(f"{Str[i-j]}",end="")
    print()

Str="NADEEM"
Length=len(Str)
for i in range(len(Str)):
    for j in range(len(Str)):
        print(f" {Str[Length-j-1]}",end="")
    print()

Str="NADEEM"
Length=len(Str)
for i in range(Length):
    for j in range(i+1):
        print(f" {Str[i]}",end="")
    print()

Str="NADEEM"
Length=len(Str)
for i in range(Length):
    for j in range(i+1):
        print(f" {Str[j]}",end="")
    print()

Str="NADEEM"
Length=len(Str)
for i in range(Length):
    for j in range(Length):
        if i==0 or i==Length-1 or j==0 or j==Length-1:
            print(Str[j],end="")
        else:
            print(" ",end="")
    print()

Str="NADEEM"
Length=len(Str)
mid=Length//2
for i in range(Length):
    for j in range(Length):
        if i == mid:
            print(Str[j], end=" ")
        elif j == mid:
            print(Str[i], end=" ")
        else:
            print("  ", end="")
    print()


n=int(input("Enter the value of n : "))
value=1
for i in range (1,n+1):
    for j in range(i):
        print(f"{value**2} ",end="")
        value+=1
    print()
