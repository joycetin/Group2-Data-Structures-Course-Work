#Question2
#The Node class represents a single node in the linked list. 
#Each node has two attributes: data and next. The data attribute stores the value ordata
#associated with the node, and the next attribute is a reference to the next node in the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# The traverse_linked_list function takes the head node of a linked list as an argument
# and traverses through the linked list, printing the data of each node. It starts by initializing a variable current
# with the value of the head node. Then, it enters a loop that continues as long as current is not None,
#  indicating there are more nodes to traverse. Inside the loop, it prints the data attribute of the current node
#  and updates current to point to the next node by assigning current.next to it. This process continues until current
#  becomes None, indicating the end of the linked list.       

def traverse_linked_list(head):
    current = head

    while current is not None:
        print(current.data)
        current = current.next

# Example usage:
# Create a linked list: 1 -> 2 -> 3 -> None
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3

# Traverse the linked list
#  Finally, the traverse_linked_list function is called with the head node (node1) to
#   print the elements of the linked list: 1, 2, 3.
traverse_linked_list(node1)

#Question4
def search(list1, n):
    low = 0
    high = len(list1)-1
    mid = 0
    while low <= high:
            # for get integer result
        mid = (high + low)//2
             # Check if n is present at mind
        if list1[mid]<n:
            low = mid + 1
        # If n is greater, compare to the right of mind
        elif list1[mid]>n:
            high = mid - 1
       # If n is smaller, compared to the left of mid
        else:
            return mid
        #element was not present in the list, return -1
    return -1
    #initial list1
list1 = [12, 24, 32,39, 45, 50, 54]
n= 45

#Function call
result = search(list1, n)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in list1")

# Question15
# The Node class represents a node in the circular linked list and has two 
# attributes; data which holds the value of the node and next
#  which points to the next node in a list.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# The CircularLinkedList class serves as the container for the circular linked list. 
# and has one attribute head, which represents the first
#  node of the list. Initially, it is set to None, indicating an empty list
class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Function to check if the list is empty by examining if the head is None or not
    def is_empty(self):
        return self.head is None

    # Function to insert an element at the beginning of the list
    #The insert_at_beginning method adds a new node with the specified data at the beginning of the list
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
            self.head = new_node

    # Function to insert an element at the end of the list
   #The insert_at_end method adds a new node with the specified data at the end of the list
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    # Function to delete a specific element from the list
     #The delete method removes the first occurrence of a node with the specified data from the list
    def delete(self, data):
        if self.is_empty():
            print("The list is empty.")
            return

        # Case 1: Deleting the head node
        if self.head.data == data:
            if self.head.next == self.head:
                self.head = None
            else:
                temp = self.head
                while temp.next != self.head:
                    temp = temp.next
                temp.next = self.head.next
                self.head = self.head.next

        # Case 2: Deleting a non-head node
        else:
            prev = None
            curr = self.head
            while curr.next != self.head:
                if curr.data == data:
                    break
                prev = curr
                curr = curr.next
            if curr.data != data:
                print("Element not found in the list.")
                return
            prev.next = curr.next

    # Function to display the elements of the list
    #The display method prints the elements of the list in order. It starts from the head and continues
    #printing the data of each node until it reachesthe head again, indicating the completion of one cycle
    def display(self):
        if self.is_empty():
            print("The list is empty.")
            return

        temp = self.head
        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.head:
                break
        print()


# Example usage:
cll = CircularLinkedList()

# Insert elements at the beginning
cll.insert_at_beginning(10)
cll.insert_at_beginning(20)
cll.insert_at_beginning(30)

# Display the list
cll.display()  # Output: 30 20 10

# Insert elements at the end
cll.insert_at_end(40)
cll.insert_at_end(50)

# Display the list
cll.display()  # Output: 30 20 10 40 50

# Delete an element
cll.delete(20)

# Display the updated list
cll.display()  # Output: 30 10 40 50