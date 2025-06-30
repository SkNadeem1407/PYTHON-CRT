class Stack:
    def __init__(self):
        self.Stack=[]
    def push(self,data):
        self.Stack.append(data)
        print("Element is appended")
    def isempty(self):
        if len(self.Stack)==0:
            return True
        return None
    def pop(self):
        if self.isempty():
            print("Stack is empty")
        else:
            self.Stack.pop()
            print("Element is removed")
    def display(self):
        for i in self.Stack:
            print(i)
Stack=Stack()
Stack.push(10)
Stack.push(20)
Stack.push(30)
Stack.push(40)
Stack.push(50)
Stack.display()
Stack.pop()
for i in list(Stack.Stack):
    print(i)




