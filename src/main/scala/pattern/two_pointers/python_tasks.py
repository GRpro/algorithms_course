# Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.
from collections import deque


def pair_with_targetsum(arr, target_sum):
    i = 0
    j = len(arr) - 1

    while i < j:
        if arr[i] + arr[j] > target_sum:
            j -= 1
        elif arr[i] + arr[j] < target_sum:
            i += 1
        else:
            return [i, j]

    return [-1, -1]


# Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; after removing the duplicates in-place return the length of the subarray that has no duplicate in it.
def remove_duplicates(arr):
    if len(arr) == 0:
        return -1
    j = 0
    res = 1
    for i in range(len(arr)):
        if arr[i] != arr[j]:
            j = i
            res += 1

    return res


# Given a sorted array, create a new array containing squares of all the numbers of the input array in the sorted order.
def make_squares(arr):
    squares = []
    i = 0
    j = len(arr) - 1

    while i <= j:
        a = arr[i] * arr[i]
        b = arr[j] * arr[j]

        if a > b:
            squares.insert(0, a)
            i += 1
        else:
            squares.insert(0, b)
            j -= 1

    return squares


# Given an array of unsorted numbers, find all unique triplets in it that add up to zero.
def search_triplets(arr):
    triplets = []

    def search_pair(arr, target_sum, left, right):
        while left < right:
            res = arr[left] + arr[right]
            if res == target_sum:
                triplets.append([-target_sum, arr[left], arr[right]])
                left += 1
                right -= 1
                while left < right and arr[left] == arr[left - 1]:
                    left += 1  # skip same element to avoid duplicate triplets
                while left < right and arr[right] == arr[right + 1]:
                    right -= 1  # skip same element to avoid duplicate triplets
            elif res > target_sum:
                right -= 1
            else:
                # res < target_sum
                left += 1

    arr.sort()

    for k in range(len(arr)):
        if k > 0 and arr[k] == arr[k - 1]:  # skip same element to avoid duplicate triplets
            continue
        search_pair(arr, -arr[k], k + 1, len(arr) - 1)

    return triplets


# Given an array arr of unsorted numbers and a target sum, count all triplets in it such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices. Write a function to return the count of such triplets.
def triplet_with_smaller_sum(arr, target):
    count = 0

    def search_pair(arr, target, left, right):
        count = 0
        while left < right:
            res = arr[left] + arr[right]
            if res < target:
                count += right - left
                left += 1
                right -= 1
            else:  # res >= target_sum
                right -= 1
        return count

    arr.sort()

    for k in range(len(arr) - 2):
        count += search_pair(arr, target - arr[k], k + 1, len(arr) - 1)

    return count


# Given an array with positive numbers and a positive target number, find all of its contiguous subarrays whose product is less than the target number.
def find_subarrays(arr, target):
    result = []

    for i in range(len(arr)):
        tmp = []
        p = 1
        j = i

        while j < len(arr) and p < target:
            p = p * arr[j]
            if p < target:
                tmp.append(arr[j])
                result.append(tmp.copy())
            j += 1

    return result


# Given an array containing 0s, 1s and 2s, sort the array in-place. You should treat numbers of the array as objects, hence, we can’t count 0s, 1s, and 2s to recreate the array.
def dutch_flag_sort(arr):
    # all elements < low are 0, and all elements > high are 2
    # all elements from >= low < i are 1
    low, high = 0, len(arr) - 1
    i = 0
    while (i <= high):
        if arr[i] == 0:
            arr[i], arr[low] = arr[low], arr[i]
            # increment 'i' and 'low'
            i += 1
            low += 1
        elif arr[i] == 1:
            i += 1
        else:  # the case for arr[i] == 2
            arr[i], arr[high] = arr[high], arr[i]
            # decrement 'high' only, after the swap the number at index 'i' could be 0, 1 or 2
            high -= 1


# Given an array of unsorted numbers and a target number, find all unique quadruplets in it, whose sum is equal to the target number.
def search_quadruplets(arr, target):
    quadruplets = []

    def search_pair(arr, target_sum, left, right):
        targets = []
        while left < right:
            res = arr[left] + arr[right]
            if res == target_sum:
              targets.append([arr[left], arr[right]])
              left += 1
              right -= 1
              while left < right and arr[left] == arr[left - 1]:
                left += 1  # skip same element to avoid duplicate triplets
              while left < right and arr[right] == arr[right + 1]:
                right -= 1  # skip same element to avoid duplicate triplets
            elif res > target_sum:
              right -= 1
            else:
              # res < target_sum
              left += 1

        return targets

    arr.sort()
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        if arr[i] > target:
            break

        for j in range(i + 1, len(arr)):
            if j > i + 1 and arr[j] == arr[j - 1]:
                continue
            if arr[i] + arr[j] > target:
                break
            pairs = search_pair(arr, target - arr[i] - arr[j], j + 1, len(arr) - 1)
            for p in pairs:
              quadruplets.append([arr[i], arr[j], p[0], p[1]])

    return quadruplets


def backspace_compare(str1, str2):
    stack1 = deque()
    stack2 = deque()

    for i in range(len(str1)):
        if str1[i] == '#':
            stack1.pop()
        else:
            stack1.append(str1[i])

    for i in range(len(str2)):
        if str2[i] == '#':
            stack2.pop()
        else:
            stack2.append(str2[i])

    if len(stack1) != len(stack2):
        return False
    else:
        for (a, b) in zip(stack1, stack2):
            if a != b:
                return False
        return True


# Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.
def shortest_window_sort(arr):
    positions = {k: idx for (idx, k) in enumerate(arr)}
    # (idx, key)
    sorted_arr = sorted(enumerate(arr), key=lambda k: k[1])

    i = 0
    while i < len(arr) and i == positions[sorted_arr[i][1]]:
        i += 1

    j = len(arr) - 1
    while j >= 0 and j == positions[sorted_arr[j][1]]:
        j -= 1

    if j >= i:
        return j - i + 1
    else:
        return 0

if __name__ == '__main__':
    # print(pair_with_targetsum([1, 2, 3, 4, 6], target_sum=6))
    #
    # print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    # print(remove_duplicates([2, 2, 2, 11]))
    #
    # print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
    # print(search_triplets([-5, 2, -1, -2, 3]))
    #
    # print(triplet_with_smaller_sum([-1, 0, 2, 3], target=3))
    # print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], target=5))
    #
    # print(find_subarrays([2, 5, 3, 10], target=30))
    # print(find_subarrays([8, 2, 6, 5], target=50))

    # arr = [1, 0, 2, 1, 0]
    # dutch_flag_sort(arr)
    # print(arr)
    # arr = [2, 2, 0, 1, 2, 0]
    # dutch_flag_sort(arr)
    # print(arr)

    # print(search_quadruplets([4, 1, 2, -1, 1, -3], target=1))
    # print(search_quadruplets([2, 0, -1, 1, -2, 2], target=2))

    # print(backspace_compare(str1="xy#z", str2="xzz#"))
    # print(backspace_compare(str1="xy#z", str2="xyz#"))
    # print(backspace_compare(str1="xp#", str2="xyz##"))
    # print(backspace_compare(str1="xywrrmp", str2="xywrrmu#p"))

    print(shortest_window_sort([1, 2, 5, 3, 7, 10, 9, 12]))
    print(shortest_window_sort([1, 3, 2, 0, -1, 7, 10]))
    print(shortest_window_sort([1, 2, 3]))
    print(shortest_window_sort([3, 2, 1]))
