# We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’.
# The array originally contained all the numbers from 1 to ‘n’, but due to a data error,
# one of the numbers got duplicated which also resulted in one number going missing. Find both these numbers.


def find_corrupt_numbers(nums):
    i, n = 0, len(nums)

    dup = None
    while i < n:
        if nums[i] != i + 1:
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                dup = nums[i]
                i += 1
        else:
            i += 1

    for i in range(n):
        if i + 1 != nums[i]:
            return [dup, i + 1]
    return [-1, -1]


if __name__ == '__main__':
    print(find_corrupt_numbers([3, 1, 2, 5, 2]))
    print(find_corrupt_numbers([3, 1, 2, 3, 6, 4]))