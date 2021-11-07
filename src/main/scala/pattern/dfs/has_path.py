class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Given a binary tree and a number ‘S’, find if the tree has a path from
# root-to-leaf such that the sum of all the node values of that path equals ‘S’.
def has_path(root, sum):
    if root is None:
        return False

    def traverse(node, cur_sum):
        if cur_sum + node.val == sum:
            return True

        new_sum = cur_sum + node.val

        res = False
        if node.left is not None:
            res = res or traverse(node.left, new_sum)
        if node.right is not None:
            res = res or traverse(node.right, new_sum)
        return res

    return traverse(root, 0)


if __name__ == '__main__':

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has path: " + str(has_path(root, 23)))
    print("Tree has path: " + str(has_path(root, 16)))

