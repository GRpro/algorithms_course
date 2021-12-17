
# Given an array of numbers sorted in an ascending order, find the ceiling of a given number ‘key’.
# The ceiling of the ‘key’ will be the smallest element in the given array greater than or equal to the ‘key’.
#
# Write a function to return the index of the ceiling of the ‘key’. If there isn’t any ceiling return -1.
def search_ceiling_of_a_number(arr, key):

    def search(lo, hi):
        if lo >= hi:
            return -1
        else:
            mid = (lo + hi) // 2
            if arr[mid] >= key:
                if mid > 0:
                    if arr[mid - 1] < key:
                        return mid
                    else:
                        return search(lo, mid)
                else:
                    return 0
            else:
                return search(mid + 1, hi)

    return search(0, len(arr))


if __name__ == '__main__':
    print(search_ceiling_of_a_number([4, 6, 10], 6))
    print(search_ceiling_of_a_number([1, 3, 8, 10, 15], 12))
    print(search_ceiling_of_a_number([4, 6, 10], 17))
    print(search_ceiling_of_a_number([4, 6, 10], -1))
    print(search_ceiling_of_a_number([4], -1))
    print(search_ceiling_of_a_number([4], 5))
    print(search_ceiling_of_a_number([4], 4))
