from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


# Given the head of a Singly LinkedList and a number ‘k’, rotate the LinkedList to the right by ‘k’ nodes.
def rotate(head, rotations):
    if head is None or rotations < 1:
        return head

    size = 0
    node = head
    while node is not None:
        node = node.next
        size += 1

    k = rotations % size

    # last part
    j = size - k
    node = head
    prev = None
    while j > 0:
        prev = node
        node = node.next
        j -= 1
    prev.next = None

    # first part
    if node is None:
        # list stays the same
        return head

    new_head = node
    while node.next is not None:
        node = node.next

    node.next = head

    return new_head


if __name__ == '__main__':

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = rotate(head, 4)
    print("Nodes of rotated LinkedList are: ", end='')
    result.print_list()

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = rotate(head, 10)
    print("Nodes of rotated LinkedList are: ", end='')
    result.print_list()
