
# We are given an unsorted array containing numbers taken from the range 1 to ‘n’.
# The array can have duplicates, which means some numbers will be missing. Find all those missing numbers.
def find_missing_numbers(nums):
    missingNumbers = []
    n = len(nums)
    i = 0
    while i < n:
        j = nums[i] - 1
        if nums[i] != i + 1 and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i, k in enumerate(nums):
        if k != i + 1:
            missingNumbers.append(i + 1)
    return missingNumbers


if __name__ == '__main__':
    print(find_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]))
    print(find_missing_numbers([2, 4, 1, 2]))
    print(find_missing_numbers([2, 3, 2, 1]))