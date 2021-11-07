class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Given a binary tree where each node can only have a digit (0-9) value, each root-to-leaf path will represent a number.
# Find the total sum of all the numbers represented by all paths.
def find_sum_of_path_numbers(root):

    def traverse(node, cur_sum) -> int:
        cur_sum = cur_sum * 10 + node.val

        if node.left is None and node.right is None:
            return cur_sum

        res = 0
        if node.left is not None:
            res += traverse(node.left, cur_sum)
        if node.right is not None:
            res += traverse(node.right, cur_sum)

        return res

    if root is None:
        return 0
    return traverse(root, 0)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))
