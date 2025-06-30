n=int(input("Enter the number of elements: "))
numbers=[]
for i in range(n):
    num=float(input("Enter the numbers: "))
    numbers.append(num)
divisor=float(input("Enter the divisor: "))
if divisor!=0:
    result=[num/divisor for num in numbers]
    print("Result after division:",result)
else:
    print("Error")
