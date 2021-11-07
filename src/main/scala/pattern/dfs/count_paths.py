class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Given a binary tree and a number ‘S’, find all paths in the tree such that the sum of all
# the node values of each path equals ‘S’. Please note that the paths can start or end at any
# node but all paths must follow direction from parent to child (top to bottom).
def count_paths(root, S):
    result = []

    def traverse(node, path, idx, cur_sum):
        if node is None:
            return

        # add cur element
        path.append(node.val)

        cur_sum += node.val
        if cur_sum == S:
            result.append(path[idx:len(path)].copy())

        while cur_sum > S:
            el = path[idx]
            cur_sum -= el
            idx += 1

        traverse(node.left, path, idx, cur_sum)
        traverse(node.right, path, idx, cur_sum)

        # remove cur element
        del path[len(path) - 1]

    traverse(root, [], 0, 0)
    return result


if __name__ == '__main__':

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has paths: " + str(count_paths(root, 11)))

