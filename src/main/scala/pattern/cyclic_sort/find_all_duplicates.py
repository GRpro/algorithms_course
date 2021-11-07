# We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’.
# The array has some numbers appearing twice,
# find all these duplicate numbers without using any extra space.

def find_all_duplicates(nums):
    duplicateNumbers = []
    i = 0
    n = len(nums)
    while i < n:
        if nums[i] != i + 1:
            j = nums[i] - 1
            if nums[i] == nums[j]:
                duplicateNumbers.append(nums[i])
                i += 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    return duplicateNumbers


if __name__ == '__main__':
    print(find_all_duplicates([3, 4, 4, 5, 5]))
    print(find_all_duplicates([5, 4, 7, 2, 3, 5, 3]))

