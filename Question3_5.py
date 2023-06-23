# 5. Write an algorithm to delete a node from a singly linked list at any position.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def deleteNode(self, position):
        if self.head is None:
            return
        if position == 0:
            self.head = self.head.next
            return self.head
        index = 0
        current = self.head
        prev = self.head
        temp = self.head
        while current is not None:
            if index == position:
                temp = current.next
                break
            prev = current
            current = current.next
            index += 1
        prev.next = temp
        return prev

    def printList(self):
        temp = self.head
        while(temp):
            print (" %d " % (temp.data),end=" ")
            temp = temp.next

llist = SinglyLinkedList()
llist.push(7)
llist.push(2)
llist.push(5)
llist.push(1)

print ("Created Linked List: ")
llist.printList()
llist.deleteNode(2)
print ("\nLinked List after Deletion at position 4: ")
llist.printList()