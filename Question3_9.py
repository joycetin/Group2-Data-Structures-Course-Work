# Write an algorithm to insert a node into a doubly linked list at the front.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_front(self, data):
        new_node = Node(data)

        if self.head is not None:
            self.head.prev = new_node
            new_node.next = self.head
            new_node.prev = None
        self.head = new_node

    def printList(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

llist = DoublyLinkedList()
llist.insert_front(2)
llist.insert_front(5)
llist.insert_front(7)
llist.insert_front(8)
llist.insert_front(3)
llist.printList()

        

 
    
