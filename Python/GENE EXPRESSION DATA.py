n=int(input("Enter the given count of data : " ))
result=[]
for i in range(n):
    temp=float(input("Enter the values: "))
    result.append(temp)
    if temp<5:
        result.append("Underexpressed")
    elif 5<= temp <=15:
        result.append("Normal")
    elif temp>15:
        result.append("Overexpressed")
    else:
        result.append("overexpressed")
print(result)