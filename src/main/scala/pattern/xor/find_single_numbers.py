# In a non-empty array of numbers, every number appears exactly twice except two numbers that appear only once. Find the two numbers that appear only once.
def find_single_numbers(nums):
    if len(nums) < 2:
        return [-1, -1]

    xor = nums[0]
    for e in nums[1:]:
        xor = e ^ xor

    diff_bit_number = 1
    while (xor & diff_bit_number) == 0:
        diff_bit_number = diff_bit_number << 1

    print("{0:b}".format(xor))
    print(diff_bit_number)

    num1 = 0
    num2 = 0
    for e in nums:
        if (e & diff_bit_number) != 0:
            num1  = e ^ num1
        else:
            num2 = e ^ num2

    return [num1, num2]


if __name__ == '__main__':

    print('Single numbers are:' +
          str(find_single_numbers([1, 4, 2, 1, 3, 5, 6, 2, 3, 5])))
    print('Single numbers are:' + str(find_single_numbers([2, 1, 3, 2])))

