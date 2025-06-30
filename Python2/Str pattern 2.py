str="ABCDE"
length=len(str)
for i in range(length):
    for ch in str:
        print(f" {ch}", end="")
    print()

str = "ABCDE"
length = len(str)
for i in range(length):
    print(" ".join(str))



str="abcde"
length=len(str)
for i in range(length):
    for j in range(i+1):
     for ch in str:
        print(f" {ch}", end="")
    print()
