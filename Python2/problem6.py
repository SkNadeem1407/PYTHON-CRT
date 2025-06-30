list=[]
for i in range(10):
    temp=input(f"enter the (i+1)song name : ")
    list.append(temp)
print(f"list in normal order:{list}")
print("list in reverse order:",list[::-1])