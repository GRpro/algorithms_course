from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_successor(root, key):
    if root is None:
        return None
    q = deque()
    q.append(root)

    node_found = False
    while len(q) > 0:
        size = len(q)
        for _ in range(size):
            node = q.popleft()

            if node_found:
                return node
            else:
                if node.val == key:
                    node_found = True
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)

    return None


if __name__ == '__main__':

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    result = find_successor(root, 12)
    if result:
        print(result.val)
    result = find_successor(root, 9)
    if result:
        print(result.val)
