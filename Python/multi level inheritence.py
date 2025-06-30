class Grandfather:
    def __init__(self):
        pass
    @staticmethod
    def properties():
        print("100 acres of land")
class Father(Grandfather):
    def __init__(self):
        super().__init__()
    @staticmethod
    def properties():
        print("50 acres of land")
class Yourself(Father):
    def __init__(self):
        super().__init__()
    @staticmethod
    def properties():
        print("DataAnalyst")
Grandfather.properties()
Father.properties()
Yourself.properties()

