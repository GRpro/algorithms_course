from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


# Given a binary tree, populate an array to represent the averages of all of its levels.
def find_level_averages(root):
    if root is None:
        return []
    result = []
    q = deque()
    q.append(root)
    while len(q) > 0:
        size = len(q)
        sum = 0
        for _ in range(size):
            node = q.popleft()
            sum += node.val
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
        result.append(sum / size)

    return result


if __name__ == '__main__':

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level averages are: " + str(find_level_averages(root)))

