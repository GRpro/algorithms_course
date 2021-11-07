from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


# Find the minimum depth of a binary tree. The minimum depth is the number of
# nodes along the shortest path from the root node to the nearest leaf node.
def find_minimum_depth(root):
    if root is None:
        return 0

    q = deque()
    q.append(root)
    result = 1

    while len(q) > 0:
        size = len(q)

        for _ in range(size):
            node = q.popleft()

            if node.left is None and node.right is None:
                return result
            else:
                if node.left is not None:
                    q.append(node.left)

                if node.right is not None:
                    q.append(node.right)
        result += 1

    return result


if __name__ == '__main__':

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
