class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1, l2):
    # Create a dummy node to serve as the head of the merged list
    dummy = ListNode()
    current = dummy

    # Traverse both lists until either one becomes None
    while l1 is not None and l2 is not None:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    # Append the remaining nodes from the non-empty list
    if l1 is not None:
        current.next = l1
    if l2 is not None:
        current.next = l2

    # Return the head of the merged list (excluding the dummy node)
    return dummy.next

# Create linked list 1: 1 -> 3 -> 10
l1 = ListNode(1)
l1.next = ListNode(3)
l1.next.next = ListNode(10)

# Create linked list 2: 5 -> 6 -> 9
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(9)

# Merge the two lists
merged = mergeTwoLists(l1, l2)

# Traverse and print the merged list: 1 -> 3 -> 5 -> 6 -> 9 -> 10
current = merged
while current is not None:
    print(current.val, end=" ")
    current = current.next
