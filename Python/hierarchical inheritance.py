class graduation:
    def __init__(self):
        pass
    @staticmethod
    def graduate():
        print("congratulations you are a graduate now")
#first subclass
class cse(graduation):
    def __init__(self):
        pass
    @staticmethod
    def graduate():
        print("congratulations you are a computer science graduate now")
#second subclass
class bioinformatics(graduation):
    def __init__(self):
        pass
    @staticmethod
    def graduate():
        print("congratulations you are a bioinformatics now")
#third subclass
class ece(graduation):
    def __init__(self):
        pass
    @staticmethod
    def graduate():
        print("congratulations you are a ece now")
graduation.graduate()
cse.graduate()
bioinformatics.graduate()
ece.graduate()

