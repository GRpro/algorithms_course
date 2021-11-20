"""
    Creating the tree - O(n) time.
    Query and updates - O(log n).
"""


# Segment tree node
class Node(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = 0
        self.left = None
        self.right = None


class SegmentTree(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """

        # helper function to create the tree from input array
        def createTree(nums, l, r):
            # base case
            if l > r:
                return None

            # leaf node
            if l == r:
                n = Node(l, r)
                n.total = nums[l]
                return n

            mid = (l + r) // 2

            node = Node(l, r)

            # recursively build the Segment tree
            node.left = createTree(nums, l, mid)
            node.right = createTree(nums, mid + 1, r)

            # Total stores the sum of all leaves under root
            # i.e. those elements lying between (start, end)
            node.total = node.left.total + node.right.total

            return node

        self.root = createTree(nums, 0, len(nums) - 1)

    def update(self, i, val):
        """
        Update i-th element, set it to val
        :type i: int
        :type val: int
        :rtype: int
        """

        def updateVal(node, i, val):
            if node.start == node.end:
                node.total = val
                return val

            mid = (node.start + node.end) // 2

            # If the index is less than the mid, that leaf must be in the left subtree
            if i <= mid:
                updateVal(node.left, i, val)

            # Otherwise, the right subtree
            else:
                updateVal(node.right, i, val)

            # Propagate the changes after recursive call returns
            node.total = node.left.total + node.right.total

            return node.total

        return updateVal(self.root, i, val)

    def sum(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """

        # Helper function to calculate range sum
        def rangeSum(root, i, j):

            # If the range exactly matches the root, we already have the sum
            if root.start == i and root.end == j:
                return root.total

            mid = (root.start + root.end) // 2

            # If end of the range is less than the mid, the entire interval lies
            # in the left subtree
            if j <= mid:
                return rangeSum(root.left, i, j)

            # If start of the interval is greater than mid, the entire interval lies
            # in the right subtree
            elif i >= mid + 1:
                return rangeSum(root.right, i, j)

            # Otherwise, the interval is split. So we calculate the sum recursively,
            # by splitting the interval
            else:
                return rangeSum(root.left, i, mid) + rangeSum(root.right, mid + 1, j)

        return rangeSum(self.root, i, j)


if __name__ == '__main__':
    tree = SegmentTree([3, 2, 3, -1, 4, 7])
    print(tree.sum(0, 2))
    tree.update(1, -3)
    print(tree.sum(0, 2))