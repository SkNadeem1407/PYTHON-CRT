list=[5,5,19,19,2,2]
print("original list :")
print(list)
new_list=[]
for i in list:
    if i not in new_list:
        new_list.append(i)
print(new_list)
