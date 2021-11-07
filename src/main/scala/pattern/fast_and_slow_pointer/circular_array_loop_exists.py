
def step(arr, idx):
    v = arr[idx]
    if v + idx >= len(arr):
        return (v + idx) % len(arr)
    elif v + idx < 0:
        return (v + idx) % len(arr)
    else:
        return v + idx


# We are given an array containing positive and negative numbers. Suppose the array contains a number ‘M’ at a particular index. Now, if ‘M’ is positive we will move forward ‘M’ indices and if ‘M’ is negative move backwards ‘M’ indices. You should assume that the array is circular which means two things:
# If, while moving forward, we reach the end of the array, we will jump to the first element to continue the movement.
# If, while moving backward, we reach the beginning of the array, we will jump to the last element to continue the movement.
# Write a method to determine if the array has a cycle. The cycle should have more than one element and should follow one direction which means the cycle should not contain both forward and backward movements.
def circular_array_loop_exists(arr):
    if len(arr) == 0:
        return False

    def can_step(idx, current_direction):
        return arr[idx] > 0 and current_direction

    idx = 0
    while idx < len(arr):
        is_ahead = arr[idx] > 0
        slow, fast = idx, idx
        while can_step(fast, is_ahead) and can_step(step(arr, fast), is_ahead):
            slow = step(arr, slow)
            fast = step(arr, step(arr, fast))
            if arr[slow] == arr[fast]:
                return True
        idx += 1

    return False


if __name__ == '__main__':
    assert step([1, 2, -4, 2, 2], 2) == 3
    assert step([1, 2, -1, 2], 1) == 3
    assert step([1, 2, 3], 2) == 2

    print(circular_array_loop_exists([1, 2, -1, 2, 2]))
    print(circular_array_loop_exists([2, 2, -1, 2]))
    print(circular_array_loop_exists([2, 1, -1, -2]))

