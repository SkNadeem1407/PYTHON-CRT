'''def multiplication_table(num):
    for i in range(1,num+1):
     for j  in  range(1,11):
        print(f"{i}*{j}={i*j}")
        print()
multiplication_table(8)'''


def multiplication_table(num):
    for i in range(1,11):
        print(f"{num} * {i} = {num * i}")
multiplication_table(8)