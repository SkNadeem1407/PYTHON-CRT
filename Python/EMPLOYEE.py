'''
write a py prog to create a employee class and declare the states and create 5 objects using different constructors
'''
class Employee:
    def _init_(self,*arg):


        self.EmpName=EmpName
        self.EmpId=EmpId
        self.Job=Job
        self.Location=Location
        self.Salary=Salary
        self.Dept=Dept      
        print("Hey..! I'm a Six Parameterized Constructor")
    def _init_(self,EmpName,EmpId,Job,Location,Salary):
        self.EmpName=EmpName
        self.EmpId=EmpId
        self.Job=Job
        self.Location=Location
        self.Salary=Salary     
        print("Hey..! I'm a Five Parameterized Constructor")
    def _init_(self,EmpName,EmpId,Job,Location):
        self.EmpName=EmpName
        self.EmpId=EmpId
        self.Job=Job
        self.Location=Location   
        print("Hey..! I'm a Four Parameterized Constructor")
    def _init_(self,EmpName,EmpId,Job):
        self.EmpName=EmpName
        self.EmpId=EmpId
        self.Job=Job  
        print("Hey..! I'm a three Parameterized Constructor")
    def _init_(self,EmpName,EmpId):
        self.EmpName=EmpName
        self.EmpId=EmpId 
        print("Hey..! I'm a Two Parameterized Constructor")
    def _init_(self,EmpName):
        self.EmpName=EmpName
        print("Hey..! I'm a One Parameterized Constructor")
    def _init_(self):
        print("Hey..! I'm a No Parameterized Constructor")
Emp1=Employee()
Emp2=Employee("Jyo")
Emp3=Employee("Hari",101)
Emp4=Employee("Rev",102,"Team Lead")
Emp5=Employee("Venkat",103,"HR","Tirupati")
Emp6=Employee("Padma",104,"Developer","kadapa",25000)