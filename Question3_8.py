# Write algorithm to insert an element in sorted linked list and unsorted linked list.
# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SortedLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    # creating an insert method in which is the value to be inserted into the linked list
    def insert(self, value):
        new_node = Node(value)
        # If the linked list is empty,
        # the method sets the new node as both the head and tail node.
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        current_node = self.head
        # If the new node's value is less than the head node's value, 
        # the method sets the new node as the new head node
        if value < current_node.data:
            new_node.next = self.head
            self.head = new_node
            return
        # the method traverses the linked list until it finds 
        # the appropriate position for the new node
        while current_node.next is not None and value > current_node.next.data:
            current_node = current_node.next

        if current_node.next is not None:
            new_node.next = current_node.next

        current_node.next = new_node

        if new_node.next is None:
            self.tail = new_node
        # the method inserts the new node before that node and updates the tail node
    def printList(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
llist = SortedLinkedList()
print("Sorted Linkedlist:")
llist.insert(3)
llist.insert(1)
llist.insert(5)
llist.insert(2)
llist.printList()
print("Unsorted Linkedlist:")
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class UnsortedLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node

    def printList(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
llist = UnsortedLinkedList()
llist.insert(3)
llist.insert(1)
llist.insert(5)
llist.insert(2)
llist.printList()
