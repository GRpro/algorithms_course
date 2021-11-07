import math


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Find the path with the maximum sum in a given binary tree. Write a function that returns the maximum sum.
# A path can be defined as a sequence of nodes between any two nodes and doesn’t necessarily pass through the root.
# The path must contain at least one node.
def find_maximum_path_sum(root):

    max_sum = -math.inf

    def traverse(node) -> int:
        nonlocal max_sum

        if node is None:
            return 0

        left_max_sum = max(traverse(node.left), 0)
        right_max_sum = max(traverse(node.right), 0)

        s = node.val + left_max_sum + right_max_sum
        print(f"node {node.val} sum {s}")
        if s > max_sum:
            max_sum = s

        return node.val + max(left_max_sum, right_max_sum)

    traverse(root)

    return max_sum


if __name__ == '__main__':

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    print("Maximum Path Sum: " + str(find_maximum_path_sum(root)))
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.left = TreeNode(9)
    print("Maximum Path Sum: " + str(find_maximum_path_sum(root)))

    root = TreeNode(-1)
    root.left = TreeNode(-3)
    print("Maximum Path Sum: " + str(find_maximum_path_sum(root)))
