from heapq import *

def find_Kth_smallest_number(nums, k):
    max_heap = []

    for n in nums:
        if len(max_heap) >= k:
            if -max_heap[0] > n:
                heappop(max_heap)
                heappush(max_heap, -n)
        else:
            heappush(max_heap, -n)
    return -max_heap[0]


if __name__ == '__main__':

    print("Kth smallest number is: " +
          str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 3)))

    # since there are two 5s in the input array, our 3rd and 4th smallest numbers should be a '5'
    print("Kth smallest number is: " +
          str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 4)))

    print("Kth smallest number is: " +
          str(find_Kth_smallest_number([5, 12, 11, -1, 12], 3)))
