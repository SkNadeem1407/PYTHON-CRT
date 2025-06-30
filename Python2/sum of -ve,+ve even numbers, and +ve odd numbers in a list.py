n=[-5,10,15,-9,22,45,-15,50,73]
sum_negative=0
sum_positive_even=0
sum_positive_odd=0
for i in (n):
    if i<=0:
        sum_negative+=i
    elif i>0 and i%2==0:
        sum_positive_even+=i
    elif i>0 and i%2!=0:
        sum_positive_odd+=i
print("sum negative:",{sum_negative})
print("sum positive:",{sum_positive_even})
print("sum odd:",{sum_positive_odd})