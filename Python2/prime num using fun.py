def prime_num(num):
    count = 0
    for i in range(1,num+1):
        if (num%i==0):
         count+=1
    if count>2:
        print(f"{num} is not a prime")
    else:
        print(f"{num} is a prime")
prime_num(6)
prime_num(68)
