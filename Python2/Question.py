'''Str=input("Enter the name with prefix(Ms/Mr): ")
if Str.startswith('Ms'):
    print("Female")
else:
    print("Male")'''

#Question 2 print count of upper and lower cases of both vowels and consonants
'''Str=input("Enter the string: ")
U_Vowels,L_Vowels,U_Consonants,L_Consonants=0,0,0,0
for ch in Str:
    if(ch.isalpha and ch.isupper):
        if ch in 'AEIOU':
            U_Vowels+=1
        else:
            U_Consonants+=1
    if(ch.isalpha and ch.islower):
        if ch in 'aeiou':
            L_Vowels+=1
        else:
            L_Consonants+=1
print(f"lower case vowel count:{L_Vowels}")
print(f"upper case vowel count:{U_Vowels}")
print(f"lower case consonant count:{L_Consonants}")
print(f"upper case consonant count:{U_Consonants}")'''







Str=input("Enter the string: ")
U_Vowels,L_Vowels,U_Consonants,L_Consonants=0,0,0,0
for ch in Str:
    if(ch>='A' and ch<='Z'):
        if ch in 'AEIOU':
            U_Vowels+=1
        else:
            U_Consonants+=1
    if(ch>='a'and ch<='z'):
        if ch in 'aeiou':
            L_Vowels+=1
        else:
            L_Consonants+=1
print(f"lower case vowel count:{L_Vowels}")
print(f"upper case vowel count:{U_Vowels}")
print(f"lower case consonant count:{L_Consonants}")
print(f"upper case consonant count:{U_Consonants}")




