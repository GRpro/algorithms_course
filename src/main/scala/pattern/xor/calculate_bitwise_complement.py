import math
# For a given positive number N in base-10, return the complement of its binary representation as a base-10 integer.
def calculate_bitwise_complement(n):
    size = int(math.log2(n)) + 1

    mask = 1
    res = 0
    for i in range(size):
        res = res | ((n & mask) ^ mask)
        mask = mask << 1
    return res


if __name__ == '__main__':
    print('Bitwise complement is: ' + str(calculate_bitwise_complement(8)))
    print('Bitwise complement is: ' + str(calculate_bitwise_complement(10)))

