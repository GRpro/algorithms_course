# In a non-empty array of integers, every number appears twice except for one, find that single number.
def find_single_number(arr):
    if len(arr) < 1:
        return 0

    n = arr[0]
    for e in arr[1:]:
        n = n ^ e
    return n


if __name__ == '__main__':
    arr = [1, 4, 2, 1, 3, 2, 3]
    print(find_single_number(arr))
