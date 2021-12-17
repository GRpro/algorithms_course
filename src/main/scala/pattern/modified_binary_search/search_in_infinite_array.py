import math


class ArrayReader:

    def __init__(self, arr):
        self.arr = arr

    def get(self, index):
        if index >= len(self.arr):
            return math.inf
        return self.arr[index]


def search_in_infinite_array(reader, key):

    i = 0

    multiplier = 1
    j = 0
    while reader.get(j) < key:
        i = j + 1
        j += j * multiplier + 1
        multiplier *= 2

    print(f"i = {i}")
    print(f"j = {j}")

    while i <= j:
        mid = (i + j) // 2
        # print(f"mid {mid}")
        if reader.get(mid) > key:
            j = mid - 1
        elif reader.get(mid) < key:
            i = mid + 1
        else:
            return mid

    return -1


if __name__ == '__main__':

    reader = ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
    print(search_in_infinite_array(reader, 14))
    print(search_in_infinite_array(reader, 11))
    reader = ArrayReader([1, 3, 8, 10, 15])
    print(search_in_infinite_array(reader, 15))
    print(search_in_infinite_array(reader, 200))
