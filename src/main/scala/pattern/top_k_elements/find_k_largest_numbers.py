from heapq import *


def find_k_largest_numbers(nums, k):
    result = []

    for num in nums:
        if len(result) >= k:
            if num > result[0]:
                heappop(result)
                heappush(result, num)
        else:
            heappush(result, num)
    return list(result)


if __name__ == '__main__':

    print("Here are the top K numbers: " +
          str(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3)))

    print("Here are the top K numbers: " +
          str(find_k_largest_numbers([5, 12, 11, -1, 12], 3)))
