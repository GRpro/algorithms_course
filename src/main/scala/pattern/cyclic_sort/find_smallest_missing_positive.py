# Given an unsorted array containing numbers, find the smallest missing positive number in it.
def find_first_smallest_missing_positive(nums):
    i, n = 0, len(nums)

    while i < n:
        if 0 < nums[i] and nums[i] <= n:
            if i + 1 != nums[i]:
                j = nums[i] - 1
                if 0 <= j and j < n:
                    if nums[i] != nums[j]:
                        nums[i], nums[j] = nums[j], nums[i]
                    else:
                        i += 1
                else:
                    i += 1
            else:
                i += 1
        else:
            i += 1

    for i in range(n):
        if i + 1 != nums[i]:
            return i + 1
    return -1


if __name__ == '__main__':
    print(find_first_smallest_missing_positive([-3, 1, 5, 4, 2]))
    print(find_first_smallest_missing_positive([3, -2, 0, 1, 2]))
    print(find_first_smallest_missing_positive([3, 2, 5, 1]))
    print(find_first_smallest_missing_positive([-1, -1, -1, 0]))
    print(find_first_smallest_missing_positive([-1, -1, -1, 1]))
    print(find_first_smallest_missing_positive([-1, 4, 4, 1]))