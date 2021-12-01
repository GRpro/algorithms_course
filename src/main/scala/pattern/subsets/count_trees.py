class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Given a number ‘n’, write a function to return the count of structurally unique
# Binary Search Trees (BST) that can store values 1 to ‘n’.
def count_trees(n):
    if n == 0:
        return 1
    count = 0
    for i in range(1, n + 1):
        # making 'i' root of the tree
        countOfLeftSubtrees = count_trees(i - 1)
        countOfRightSubtrees = count_trees(n - i)
        count += (countOfLeftSubtrees * countOfRightSubtrees)
    return count


if __name__ == '__main__':

    print("Total trees: " + str(count_trees(2)))
    print("Total trees: " + str(count_trees(3)))

