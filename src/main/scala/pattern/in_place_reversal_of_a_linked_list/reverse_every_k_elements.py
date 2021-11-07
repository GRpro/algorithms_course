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


# Given the head of a LinkedList and a number ‘k’, reverse every ‘k’ sized sub-list starting from the head.
# If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse it too.
def reverse_every_k_elements(head, k):
    if k <= 1 or head is None:
        return head
    
    node = head

    prev_part_last = head
    prev_part_head = head
    p = 0
    while node is not None:
        prev = None
        node = prev_part_head

        i = 0
        while i < k and node is not None:
            i += 1
            nxt = node.next
            node.next = prev
            prev = node
            node = nxt

        if p == 0:
            head = prev
        else:
            prev_part_last.next = prev
            prev_part_last = prev_part_head

        prev_part_head.next = node
        prev_part_head = node
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
    # head.next.next.next.next.next.next.next.next = Node(9)
    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_every_k_elements(head, 3)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()
