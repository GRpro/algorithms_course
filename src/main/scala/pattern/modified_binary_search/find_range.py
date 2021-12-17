
# Given an array of numbers sorted in ascending order, find the range of a given number ‘key’.
# The range of the ‘key’ will be the first and last position of the ‘key’ in the array.
#
# Write a function to return the range of the ‘key’. If the ‘key’ is not present return [-1, -1].
def find_range(arr, key):

    def find(lo, hi, isStart):
        keyIndex = -1
        while lo <= hi:
            m = (lo + hi) // 2
            if arr[m] > key:
                hi = m - 1
            elif arr[m] < key:
                lo = m + 1
            else:
                keyIndex = m
                if isStart:
                    hi = m - 1
                else:
                    lo = m + 1
        return keyIndex

    i = find(0, len(arr) - 1, True)
    if i == -1:
        return [- 1, -1]
    else:
        j = find(i, len(arr) - 1, False)
        return [i, j]


if __name__ == '__main__':

    print(find_range([4, 6, 6, 6, 9], 6))
    print(find_range([1, 3, 8, 10, 15], 10))
    print(find_range([1, 3, 8, 10, 15], 12))
