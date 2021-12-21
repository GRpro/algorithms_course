

# Given an array of numbers which is sorted in ascending order and also rotated by some arbitrary number,
# find if a given ‘key’ is present in it.
# Write a function to return the index of the ‘key’ in the rotated array.
# If the ‘key’ is not present, return -1. You can assume that the given array does not have any duplicates
def search_rotated_array(arr, key):
    if len(arr) == 0:
        return -1

    lo = 0
    hi = len(arr) - 1


    while lo <= hi:
        m = (lo + hi) // 2

        if key == arr[m]:
            return m

        if arr[lo] == arr[m] and arr[hi] == arr[m]:
            lo += 1
            hi -= 1
        elif arr[lo] <= arr[m]:  # left side is sorted in ascending order
            if key >= arr[lo] and key < arr[m]:
                hi = m - 1
            else:  # key > arr[m]
                lo = m + 1

        else:  # right side is sorted in ascending order
            if key > arr[m] and key <= arr[hi]:
                lo = m + 1
            else:
                hi = m - 1

    return -1



if __name__ == '__main__':
    print(search_rotated_array([10], 15))
    print(search_rotated_array([10, 15, 1, 3, 8], 15))
    print(search_rotated_array([10, 15, 1, 3, 8], 3))
    print(search_rotated_array([10, 15, 1, 3, 8], 7))
    print(search_rotated_array([3, 7, 3, 3, 3], 7))
    print(search_rotated_array([4, 5, 7, 9, 10, -1, 2], 10))

