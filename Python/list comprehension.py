'''Num=[]
for i in range(1,11):
    Num.append(i)
print(Num)
#implementing Same using list comprehension
#new_list = [expression for item in iterable_object if_statement'''

n=int(input("enter the value: "))
New=[i for i in range(1,n+1) if i%2==0]
print(New)
