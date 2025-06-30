Str=input("Enter the string: ")
uppercase_alpha=0
lowercase_alpha=0
numeric=0
special_char=0
for ch in Str:
    if ch.isupper():
        uppercase_alpha+=1
    elif ch.islower():
        lowercase_alpha+=1
    elif ch.isdigit():
        numeric+=1
    else:
        special_char+=1
print(f"count of uppercase letters: {uppercase_alpha}")
print(f"count of lowercase letters:{lowercase_alpha}")
print(f"count of numeric values:{numeric}")
print(f"count of special characters:{special_char}")