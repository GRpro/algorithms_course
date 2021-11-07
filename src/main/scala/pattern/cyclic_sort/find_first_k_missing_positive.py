# Given an unsorted array containing numbers and a number ‘k’, find the first ‘k’ missing positive numbers in the array.
def find_first_k_missing_positive(nums, k):
    missingNumbers = []

    i, n = 0, len(nums)
    s = set()
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
            s.add(nums[i])
            i += 1

    for i in range(n):
        if len(missingNumbers) >= k:
            break
        if i + 1 != nums[i]:
            missingNumbers.append(i + 1)

    i = n + 1
    while len(missingNumbers) < k:
        if i not in s:
            missingNumbers.append(i)
        i += 1

    return missingNumbers

if __name__ == '__main__':
    print(find_first_k_missing_positive([3, -1, 4, 5, 5], k=3))
    print(find_first_k_missing_positive([2, 3, 4], k=3))
    print(find_first_k_missing_positive([-2, -3, 4], k=2))
    print(find_first_k_missing_positive([2, 3, 5], k=6))