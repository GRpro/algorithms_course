class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Given a binary tree, find the length of its diameter. The diameter of a tree is the number of nodes on the longest
# path between any two leaf nodes. The diameter of a tree may or may not pass through the root.
class TreeDiameter:

    def __init__(self):
        self.treeDiameter = 0

    def find_diameter(self, root):

        def traverse(node) -> int:
            if node is None:
                return 0

            left_longest = traverse(node.left)
            right_longest = traverse(node.right)

            size = 1 + left_longest + right_longest
            if size > self.treeDiameter:
                self.treeDiameter = size

            return 1 + max(left_longest, right_longest)

        traverse(root)
        return self.treeDiameter


if __name__ == '__main__':

    treeDiameter = TreeDiameter()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))
    root.left.left = None
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.left = TreeNode(9)
    root.right.left.right.left = TreeNode(10)
    root.right.right.left.left = TreeNode(11)
    print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))

