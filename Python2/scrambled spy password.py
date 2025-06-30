word = (input("Enter the spy password: "))
char_list = list(word)
print(char_list)
for i in range(len(char_list)):
    j = (i * 3 + 1) % len(char_list)
    char_list[i], char_list[j] = char_list[j], char_list[i]
print("After Swapping :")
scrambled_word = ''.join(char_list)
Temp = word
Word = char_list
char_list = Temp
print("original password:", word)
print("scrambled spy password:", scrambled_word)

