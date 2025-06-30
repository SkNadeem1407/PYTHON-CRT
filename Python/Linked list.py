
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
first=Node(10)
second=Node(20)
third=Node(30)
fourth=Node(40)
fifth=Node(50)
head=first
head.next=second
second.next=third
third.next=fourth
fourth.next=fifth
current=head
while current:
    print(current.data, end="-->")
    current=current.next
print("None")



