from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


# Given a binary tree, populate an array to represent its zigzag level order traversal.
# You should populate the values of all nodes of the first level from left to right,
# then right to left for the next level and keep alternating in the same manner for the following levels.
def traverse(root):
    result = deque()
    if root is None:
        return result

    q = deque()
    q.append(root)
    forward = True
    while len(q) > 0:
        level = deque()
        levelSize = len(q)

        for _ in range(levelSize):
            node = q.popleft()

            if forward:
                level.append(node.val)
            else:
                level.appendleft(node.val)

            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)

        result.append(list(level))
        forward = not forward

    return result


if __name__ == '__main__':

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    print("Zigzag traversal: " + str(traverse(root)))
