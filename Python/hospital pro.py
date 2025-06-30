class person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def details(Self):
        print(f"person's name :{self.name}")
        print(f"person's age :{self.age}")
        print(f"person's gender :{self.gender}")
class patient(person):
    def __init__(self,name,age,gender,disease):
        super().__init__(self,name,age,gender)
        self.disease=disease
    def details(Self):
        print(f"patient's name :{self.name}")