toy_list=[]
num=int (input("size of the lists : "))
for i in range (num):
    temp=input("enter the toy name : ")
    toy_list.append(temp)
print(f"elements of the list: {toy_list}")
new_list=[]
for i in toy_list:
    if i not in new_list:
        new_list.append(i)
new_list.sort()
print(new_list)