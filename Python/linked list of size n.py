'''
#Write a python program to create a linked list of size 'n'
take user as a input for 'n' and the elements of the linked list without using methods
'''
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
n = int(input("Enter the size of the linked list: "))
if n <= 0:
    print("Linked list size must be positive.")
else:
    data = input("Enter element 1: ")
    head = Node(data)
    current = head
    for i in range(2, n + 1):
        data = input(f"Enter element {i}: ")
        new_node = Node(data)
        current.next = new_node
        current = new_node
    print("Linked list elements:")
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next