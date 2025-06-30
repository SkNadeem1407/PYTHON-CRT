n=int(input("Enter the no.of words that you would be like to find: "))
List=['Dairy','Water','Crack','Good','Five','Jim']
Tuple=('Milk','Bottle','Jack','Day','Star','Jam')
i=1
while(i<=n):
    word=input("Enter the word: ")
    index=List.index(word)
    print(f"{word}-{Tuple[index]}")
    i+=1
