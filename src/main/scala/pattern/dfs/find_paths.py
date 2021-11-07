class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Given a binary tree and a number ‘S’, find all paths from root-to-leaf
# such that the sum of all the node values of each path equals ‘S’.
def find_paths(root, sum):
    if root is None:
        return False

    allPaths = []

    def traverse(node, cur_sum, path):
        new_sum = cur_sum + node.val
        path.append(node.val)

        if new_sum == sum:
            allPaths.append(path.copy())

        if node.left is not None:
            traverse(node.left, new_sum, path)
        if node.right is not None:
            traverse(node.right, new_sum, path)

        del path[-1]
        return

    traverse(root, 0, [])

    return allPaths


if __name__ == '__main__':

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    sum = 23
    print("Tree paths with sum " + str(sum) +
          ": " + str(find_paths(root, sum)))
