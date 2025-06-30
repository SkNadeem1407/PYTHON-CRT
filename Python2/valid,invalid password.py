'''password=(input("Enter the password: "))
upper_case=0
lower_case=0
numeric=0
special_char=0
for ch in password:
    if ch.isupper():
        upper_case+=1
    elif ch.islower():
        lower_case+=1
    elif ch.isdigit():
        numeric+=1
    else:
        special_char+=1
if (upper_case >=3) or (lower_case >=3) and (numeric >=1) and (special_char >=3):
    print("Valid password")
else:
    print("Invalid password")'''



Name=(input("Enter the name: "))
Contact=(input("Enter the contact number: "))
Mail_Id=(input("Enter the mail id:"))
Password=(input("Enter the password: "))
upper_case=0
lower_case=0
numeric=0
special_char=0
length=len(Contact)
if len(Contact)==10:
    print("Valid Contact: ")
else:
    print("Not Valid Contact: ")
for ch in Password:
    if ch.isupper():
        upper_case+=1
    elif ch.islower():
        lower_case+=1
    elif ch.isdigit():
        numeric+=1
    else:
        special_char+=1
if (upper_case >=3) or (lower_case >=3) and (numeric >=1) and (special_char >=3):
    print("Valid password")
else:
    print("Invalid password")













