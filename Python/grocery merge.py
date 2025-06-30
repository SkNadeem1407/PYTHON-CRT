list1 = ['Oil','Dal','Jeera','Wheat flour','Soaps','Toothpaste']
list2 = ['Ricebag','Onions','Toothpaste','Soaps','Oil','Dal','Jeera']
list1.extend(list2)
new_list=[]
for i in list1:
    if i not in new_list:
        new_list.append(i)
new_list.sort()
print(new_list)
