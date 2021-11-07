class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# Given the head of a Singly LinkedList, write a method to return the middle node of the LinkedList.
# If the total number of nodes in the LinkedList is even, return the second middle node.
def find_middle_of_linked_list(head):
    fast, slow = head, head
    while fast != None and fast.next != None:
        # if fast.next.next != None:
        fast = fast.next.next
        slow = slow.next

    return slow


if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Middle Node: " + str(find_middle_of_linked_list(head).value))

    head.next.next.next.next.next = Node(6)
    print("Middle Node: " + str(find_middle_of_linked_list(head).value))

    head.next.next.next.next.next.next = Node(7)
    print("Middle Node: " + str(find_middle_of_linked_list(head).value))
