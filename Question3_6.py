# Write an algorithm for deletion of node at any position from doubly linked list with
# example.
# Here is the example;
# Suppose you have the following doubly linked list: 1 <-> 2 <-> 3 <-> 4 <-> 5
# To delete the node with value 3, you would follow these steps:
# 1. Check if the linked list is empty. It is not.
# 2. Check if the node to be deleted is the head node. It is not.
# 3. Traverse the linked list to find the node with value 3.
# 4. The node to be deleted is not the last node.
# 5. Set the next node of node 2 (the previous node) to node 4 (the node after the node to be deleted).
# 6. Set the previous node of node 4 (the next node) to node 2 (the node before the node to be deleted).
# 7. Delete the node with value 3.
# 8. The updated linked list is now: 1 <-> 2 <-> 4 <-> 5


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    def print_list(self):
        if self.head == None:
            print("Empty")
        else:
            current_node = self.head
            while current_node != None:
                print(current_node.data, end= ' ')
                current_node = current_node.next
        print()

    def append(self, data):
        new_node = Node(data)
        # if linked list s empty, make head and tail both equal to the new node
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length += 1
            return
        # Else, make the previous pointer of the new node point to the present tail
        else:     
            new_node.previous = self.tail
            # make the next pointer of the present tail point to the new node establishing
            # a two way link between the present tail and the new node 
            self.tail.next = new_node 
            # finally updating the tail to be equal to the new node
            self.tail = new_node
            self.length += 1
            return
    
    def delete_by_position(self, position):
        if self.head == None:
            print("Linked List is empty, nothing to delete.")
            return
        
        if position == 0:
            self.head = self.head.next
            # print (self.head)
            if self.head == None or self.head.next == None:
                self.tail = self.head
            if self.head != None:
                # updating the previous node of the new head to be equal to None
                self.head.previous = None
            self.length -= 1
            return
        if position >= self.length:
            position = self.length-1
        
        current_node = self.head
        for i in range(position - 1):
            current_node = current_node.next
        current_node.next = current_node.next.next
        # similar logic to the delete_by_value method
        if current_node.next != None:
            current_node.next.previous = current_node
        else:
            self.tail = current_node
        self.length -= 1
        return
    
List = DoublyLinkedList()
# empty
List.print_list()
print("------------------")

List.append(7)
List.append(6)
List.append(5)
List.append(4)
List.append(3)
List.print_list()
print("------------------")

List.delete_by_position(2)
List.print_list()
print("------------------")

List.delete_by_position(0)
List.print_list()
print("------------------")

