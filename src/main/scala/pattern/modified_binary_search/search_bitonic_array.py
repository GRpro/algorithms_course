# Given a Bitonic array, find if a given ‘key’ is present in it.
# An array is considered bitonic if it is monotonically increasing and then monotonically decreasing.
# Monotonically increasing or decreasing means that for any index i in the array arr[i] != arr[i+1].
# Write a function to return the index of the ‘key’. If the ‘key’ is not present, return -1.
def search_bitonic_array(arr, key):

    # find max
    start = 0
    end = len(arr) - 1
    while start < end:
        mid = (start + end) // 2
        if arr[mid] > arr[mid + 1]:
            end = mid
        else:
            start = mid + 1

    max_el_idx = start
    print(f"max el idx {max_el_idx}")

    def binary_search(start, end, is_asc):
        while start <= end:
            mid = start + (end - start) // 2

            if key == arr[mid]:
                return mid

            if is_asc:  # ascending order
                if key < arr[mid]:
                    end = mid - 1  # the 'key' can be in the first half
                else:  # key > arr[mid]
                    start = mid + 1  # the 'key' can be in the second half
            else:  # descending order
                if key > arr[mid]:
                    end = mid - 1  # the 'key' can be in the first half
                else:  # key < arr[mid]
                    start = mid + 1  # the 'key' can be in the second half

        return -1  # element not found

    if key > max_el_idx:
        return binary_search(max_el_idx, len(arr) - 1, is_asc=False)
    else:
        return binary_search(0, max_el_idx, is_asc=True)

if __name__ == '__main__':
    print(search_bitonic_array([1, 3, 8, 4, 3], 4))
    print(search_bitonic_array([3, 8, 3, 1], 8))
    print(search_bitonic_array([1, 3, 8, 12], 12))
    print(search_bitonic_array([10, 9, 8], 10))
    print(search_bitonic_array([10, 9, 8], 7))
