#Print Natural Number from 1 to n
N=int(input("Enter the value of n: "))
def NaturalNum(N):
    if N==0:
        return
    NaturalNum(N-1)
    print(N)
NaturalNum(N)

#Print Natural Number from n to 1
N=int(input("Enter the value of n: "))
def NaturalNum(N):
    if N==0:
        return
    if N!=0:
        print(N)
    return NaturalNum(N-1)
NaturalNum(N)

