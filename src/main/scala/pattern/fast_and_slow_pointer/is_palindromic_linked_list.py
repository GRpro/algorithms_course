from collections import deque


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def is_palindromic_linked_list(head):
    if head is None or head.next is None:
        return True
    stack = deque()

    k = 0
    slow, fast = head, head
    while fast is not None:
        stack.append(slow.value)
        slow = slow.next
        fast = fast.next
        k += 1
        if fast is not None:
            k += 1
            fast = fast.next

    if k % 2 == 1:
        stack.pop()

    while slow.next is not None:
        left = stack.pop()
        right = slow.value
        if left != right:
            return False
        slow = slow.next

    return True


if __name__ == '__main__':
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)

    print("Is palindrome: " + str(is_palindromic_linked_list(head)))

    head.next.next.next.next.next = Node(2)
    print("Is palindrome: " + str(is_palindromic_linked_list(head)))
