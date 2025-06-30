size=int(input("Enter the length of list :"))
Char_List=[]
for i in range(size):
    ch=input("Enter the characters :")
    Char_List.append(ch)
print(Char_List)
Str="".join(Char_List)
print(Str)