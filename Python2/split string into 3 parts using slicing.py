Str=input("Enter the string: ")
length = len(Str)
if length%3==0:
    first_part=Str[:length//3]
    second_part=Str[length//3:2*length//3]
    third_part=Str[2*length//3:]
print(f"First part:",first_part)
print(f"Second part:",second_part)
print(f"Third part:",third_part)



