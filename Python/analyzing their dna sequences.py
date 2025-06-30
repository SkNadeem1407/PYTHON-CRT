Sequence=input("Enter the DNA sequence: ")
A_count=0
T_count=0
G_count=0
C_count=0
return_seq=[]
for base in Sequence:
    if base=='A':
        A_count+=1
    elif base=='T':
        T_count+=1
    elif base=='G':
        G_count+=1
    elif base=="C":
        C_count+=1
    else:
        print("Error sequence")
total_bases=A_count+T_count+G_count+C_count
if total_bases>0:
    GC_Content = ((G_count + C_count) / total_bases) * 100
print(f"Gc_content:{GC_Content:.2f}%")
if total_bases>60:
    print("High")
elif 40 < total_bases <= 60:
    print("Moderate")
else:
    print("Low")


