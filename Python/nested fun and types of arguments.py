'''def Eat():
    def WashHands():
        print("Wash Hands.....!")
    def ServeFood():
        print("Serve Food....!")
    WashHands()
    ServeFood()
    print("Enjoy Your Meal....!")
    WashHands()
Eat()'''

'''def Hello():
    print("Hello")
print(Hello())'''

#Positional argument
'''def pw(x,y):
    z=x**y
    print(z)
pw(5,2)'''

#Keyword arguments
'''def show(name,age):
    print(name,age)
show(name="kumar",age=22)'''

#Default arguments
'''def show(name,age=27):
    print(name,age)
show(name="Ram",age=25)'''

#Variable length
'''def display(*x):
    x=x[0]+x[1]+x[2]+x[3]+x[4]
    print(x)
display(10,10,10,10,10)'''

#Keyword Variable Length Arguments
def add(**num):
    z=num['a']+num['b']+num['c']
    print(z)
add(a=4,b=6,c=5)
