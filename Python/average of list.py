n=int(input("Enter the number of elements: "))
numbers=[]
for i in range(n):
    num=float(input("Enter a number: "))
    numbers.append(num)
    if numbers:
        average=sum(numbers)/len(numbers)
        print(f"average numbers: ", average)
    else:
        print(f"no average number")


