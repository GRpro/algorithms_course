# We are given an array containing n objects. Each object, when created, was assigned a unique number from the range 1 to n based on their creation sequence. This means that the object with sequence number 3 was created just before the object with sequence number 4.
#
# Write a function to sort the objects in-place on their creation sequence number in O(n)O(n) and without using any extra space. For simplicity, let’s assume we are passed an integer array containing only the sequence numbers, though each number is actually an object.
def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        if nums[i] == i + 1:
            i += 1
        else:
            j = nums[i]-1
            nums[i], nums[j] = nums[j], nums[i]
    return nums


if __name__ == '__main__':
    print(cyclic_sort([4, 2, 3, 1, 5]))
    print(cyclic_sort([3, 1, 5, 4, 2]))
    print(cyclic_sort([2, 6, 4, 3, 1, 5]))
    print(cyclic_sort([1, 5, 6, 4, 3, 2]))