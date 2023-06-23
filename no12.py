class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def splitLinkedList(head, condition):
    first_head = None
    second_head = None
    first_tail = None

    current = head
    prev = None

    while current is not None:
        if condition(current.val):
            if first_head is None:
                first_head = current
                first_tail = current
            else:
                first_tail.next = current
                first_tail = current

            if prev is not None:
                prev.next = None
        else:
            if second_head is None:
                second_head = current

        prev = current
        current = current.next

    return first_head, second_head

# Example usage
# Create the original linked list: 1 -> 2 -> 3 -> 4 -> 5 -> None
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Split the linked list based on the condition of even numbers
split_condition = lambda x: x % 2 == 0
first_split, second_split = splitLinkedList(head, split_condition)

# Print the first split list: 1 -> 3 -> 5 -> None
current = first_split
while current is not None:
    print(current.val, end=" ")
    current = current.next

# Print the second split list: 2 -> 4 -> None
current = second_split
while current is not None:
    print(current.val, end=" ")
    current = current.next
