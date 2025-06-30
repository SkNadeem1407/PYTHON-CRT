#duck typing
class duck:
    def walk(self):
        print("thapak thapak thapak thapak")

class horse:
    def walk(self):
        print("tabdak tabdak tabdak tabdak")
def myfunction(obj):
    obj.walk()
d = duck()
myfunction(d)
h = horse()
myfunction(h)