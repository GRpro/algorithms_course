
# Given a sorted array of numbers, find if a given number ‘key’ is present in the array.
# Though we know that the array is sorted, we don’t know if it’s sorted in ascending or descending order.
# You should assume that the array can have duplicates.
#
# Write a function to return the index of the ‘key’ if it is present in the array, otherwise return -1.
def binary_search(arr, key):
    if len(arr) <= 0:
        return -1
    elif len(arr) == 1:
        if arr[0] == key:
            return 0
        else:
            return -1
    else:

        lo = 0
        hi = len(arr) - 1

        def bin_s(lo, hi, is_asc):
            # print(f"lo {lo}   hi {hi}")
            if lo == hi:
                if arr[lo] == key:
                    return lo
                else:
                    return -1

            m = (lo + hi) // 2

            if arr[m] == key:
                return m
            else:
                if arr[m] > key:
                    if is_asc:
                        return bin_s(lo, m, is_asc)
                    else:
                        return bin_s(m + 1, hi, is_asc)
                else:  # arr[m] < key
                    if is_asc:
                        return bin_s(m + 1, hi, is_asc)
                    else:
                        return bin_s(lo, m, is_asc)

    return bin_s(lo, hi, arr[lo] < arr[hi])


if __name__ == '__main__':

    print(binary_search([4, 6, 10], 10))
    print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
    print(binary_search([10, 6, 4], 10))
    print(binary_search([10, 6, 4], 4))
    print(binary_search([10], 10))
    print(binary_search([10], 9))


