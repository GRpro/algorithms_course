class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Given a binary tree and a number sequence,
# find if the sequence is present as a root-to-leaf path in the given tree.
def find_path(root, sequence):
    seq_len = len(sequence)

    if root is None or seq_len == 0:
        return None

    def find(node, idx):
        if idx == seq_len:
            if node is None:
                return True
            else:
                return False

        if node is None:
            return False

        if node.val != sequence[idx]:
            return False

        return find(node.left, idx + 1) or find(node.right, idx + 1)

    return find(root, 0)


if __name__ == '__main__':

    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
    print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))
