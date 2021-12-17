# Given an array of numbers sorted in ascending order, find the floor of a given number ‘key’.
# The floor of the ‘key’ will be the biggest element in the given array smaller than or equal to the ‘key’
#
# Write a function to return the index of the floor of the ‘key’. If there isn’t a floor, return -1.
def search_floor_of_a_number(arr, key):

    def search(lo, hi):
        if lo >= hi:
            return -1
        else:
            mid = (lo + hi) // 2
            if arr[mid] <= key:
                if mid < len(arr) - 1:
                    if arr[mid + 1] > key:
                        return mid
                    else:
                        return search(mid, hi)
                else:
                    return mid
            else:
                return search(lo, mid - 1)

    return search(0, len(arr))


if __name__ == '__main__':

    print(search_floor_of_a_number([4, 6, 10], 6))
    print(search_floor_of_a_number([1, 3, 8, 10, 15], 12))
    print(search_floor_of_a_number([4, 6, 10], 17))
    print(search_floor_of_a_number([4, 6, 10], -1))
