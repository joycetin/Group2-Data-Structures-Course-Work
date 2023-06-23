# Node class for creating individual nodes of the doubly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# DoublyLinkedList class to perform operations on the doubly linked list
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insertion at the beginning of the list
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is not None:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node

    # Insertion at the end of the list
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    # Insertion after a specific node
    def insert_after_node(self, prev_node, data):
        if prev_node is None:
            print("Previous node is not found.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        if prev_node.next is not None:
            prev_node.next.prev = new_node
        prev_node.next = new_node
        new_node.prev = prev_node

    # Deletion of a specific node
    def delete_node(self, node):
        if self.head is None or node is None:
            return
        if self.head == node:
            self.head = node.next
        if node.next is not None:
            node.next.prev = node.prev
        if node.prev is not None:
            node.prev.next = node.next
        node.prev = None
        node.next = None
        del node

    # Display the elements of the doubly linked list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

# Example usage
dllist = DoublyLinkedList()

dllist.insert_at_beginning(3)
dllist.insert_at_beginning(2)
dllist.insert_at_beginning(1)

dllist.display()  # Output: 1 2 3

dllist.insert_at_end(4)
dllist.insert_at_end(5)

dllist.display()  # Output: 1 2 3 4 5

node2 = dllist.head.next
dllist.insert_after_node(node2, 2.5)

dllist.display()  # Output: 1 2 2.5 3 4 5

dllist.delete_node(dllist.head)
dllist.delete_node(dllist.head.next)

dllist.display()  # Output: 2.5 4 5
