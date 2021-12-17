
# Given an array of numbers sorted in ascending order,
# find the element in the array that has the minimum difference with the given ‘key’.
def search_min_diff_element(arr, key):

    i = 0
    j = len(arr) - 1
    while i <= j:
        m = (i + j) // 2
        if arr[m] < key:
            i = m + 1
        elif arr[m] > key:
            j = m - 1
        else:
            return m
    # print(f"i = {i}")
    # print(f"j = {j}")

    if j >= 0 and i < len(arr):
        if abs(arr[i] - key) < abs(arr[j] - key):
            return i
        else:
            return j
    elif i < len(arr):
        return i
    else:
        return j


if __name__ == '__main__':

    print(search_min_diff_element([4, 6, 10], 7))
    print(search_min_diff_element([4, 6, 10], 4))
    print(search_min_diff_element([1, 3, 8, 10, 15], 12))
    print(search_min_diff_element([4, 6, 10], 17))

