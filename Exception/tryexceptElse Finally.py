a=10
b=0
try:
    d=a/b
    print(d)
    print('Inside Try')
except ZeroDivisionError:
    print('Division by Zero Not Allowed')
else:
    print('Inside Else')
finally:
    print('Inside Finally')
print('Rest of the Code')