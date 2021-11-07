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


# Given the head of a LinkedList and a number ‘k’,
# reverse every alternating ‘k’ sized sub-list starting from the head.
# If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse it too.
def reverse_alternate_k_elements(head, k):
    if k <= 1 or head is None:
        return head

    prev_part_last = head

    p = 0
    node = head
    while node is not None:
        prev = None

        i = 0
        hd = node
        while i < k and node is not None:
            i += 1
            nxt = node.next
            node.next = prev
            prev = node
            node = nxt
        hd.next = node

        i = 0
        prv = prev
        while i < k and node is not None:
            prv = node
            node = node.next
            i += 1

        if p == 0:
            head = prev
        else:
            prev_part_last.next = prev

        prev_part_last = prv

        p += 1

    return head


if __name__ == '__main__':

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_alternate_k_elements(head, 2)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()

