# Write an algorithm to insert an element into unsorted linked list.
# Node structure of a linked list node 
class Node:

    def __init__(self, data):
        self.data = data 
        self.next = None 


# Linked List class contains a Node object
class UnsortedLinkedList:

    def __init__(self):
        self.head = None


    # Using this function we will be inserting new nodes at the head of the list
    def push(self, new_data):

        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Using this function we will be printing the content of the linked list
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data,end=" ")
            temp = temp.next


if __name__=='__main__':

    llist = UnsortedLinkedList()
    llist.push(3)
    llist.push(5)
    llist.push(2)
    llist.push(4)
    llist.push(8)

    print("Created UnsortedLinked list is:")
    llist.printList()