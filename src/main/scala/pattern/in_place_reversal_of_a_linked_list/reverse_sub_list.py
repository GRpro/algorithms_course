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


# Given the head of a LinkedList and two positions ‘p’ and ‘q’,
# reverse the LinkedList from position ‘p’ to ‘q’.
def reverse_sub_list(head, p, q):
    if q < 1:
        q = 1
    if p < 1:
        p = 1
    if p == q:
        return head

    prev = None
    node = head
    i = 0

    # part1
    while i < p - 1 and node is not None:
        prev = node
        node = node.next
        i += 1

    part1_last = prev
    part2_last = node

    # part2
    i = 0
    while i < q - p + 1 and node is not None:
        tmp = node.next
        node.next = prev
        prev = node
        node = tmp
        i += 1

    if part1_last is not None:
        part1_last.next = prev
    else:
        head = prev

    # part3
    part2_last.next = node

    return head


if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_sub_list(head, 2, 4)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()
