from __future__ import print_function
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


# Given a binary tree, return an array containing nodes in its right view.
# The right view of a binary tree is the set of nodes visible when the tree is seen from the right side.
def tree_right_view(root):
    result = []
    if root is None:
        return result

    q = deque()
    q.append(root)
    while len(q) > 0:
        size = len(q)
        for i in range(size):
            node = q.popleft()

            if i == size - 1:
                result.append(node)

            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
    return result


if __name__ == '__main__':

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.left.left.left = TreeNode(3)
    result = tree_right_view(root)
    print("Tree right view: ")
    for node in result:
        print(str(node.val) + " ", end='')
