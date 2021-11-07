from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


# Given a binary tree, populate an array to represent its level-by-level traversal in reverse order,
# i.e., the lowest level comes first. You should populate the values of all nodes
# in each level from left to right in separate sub-arrays.
def traverse(root):
    result = deque()
    if root is None:
        return result

    q = deque()
    q.append(root)
    while len(q) > 0:
        level = []
        levelSize = len(q)
        for _ in range(levelSize):
            node = q.popleft()
            level.append(node.val)
            if node.left is not None:
                q.append(node.left)

            if node.right is not None:
                q.append(node.right)
        result.appendleft(level)
    return result


if __name__ == '__main__':

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Reverse level order traversal: " + str(traverse(root)))
