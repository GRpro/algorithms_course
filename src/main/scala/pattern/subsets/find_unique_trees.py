from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Given a number ‘n’, write a function to return all structurally unique Binary Search Trees (BST)
# that can store values 1 to ‘n’?
def find_unique_trees(n):
    if n < 0:
        return None

    def subtrees(start, end):
        result = []

        if start > end:
            result.append(None)
            return result
        else:
            for i in range(start, end + 1):
                left_subtrees = subtrees(start, i - 1)
                right_subtrees = subtrees(i + 1, end)

                for l in left_subtrees:
                    for r in right_subtrees:
                        node = TreeNode(i)
                        node.left = l
                        node.right = r
                        result.append(node)
            return result

    return subtrees(1, n)


if __name__ == '__main__':
    print("Total trees: " + str(len(find_unique_trees(2))))
    print("Total trees: " + str(len(find_unique_trees(3))))
