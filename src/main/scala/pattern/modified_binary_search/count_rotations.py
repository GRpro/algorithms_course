def count_rotations(arr):
  if len(arr) == 0:
    return 0

  lo = 0
  hi = len(arr) - 1

  max_idx = -1
  max_el = -1

  while lo <= hi:
    m = (lo + hi) // 2
    if arr[lo] <= arr[m]:
      if max_el < arr[m]:
        max_el = arr[m]
        max_idx = m
      # no highest el in this range
      lo = m + 1
    else:
      # arr[lo] > arr[m]
      if max_el < arr[lo]:
        max_el = arr[lo]
        max_idx = lo
      hi = m - 1

  return (max_idx + 1) % len(arr)


if __name__ == '__main__':

  print(count_rotations([10, 15, 1, 3, 8]))
  print(count_rotations([4, 5, 7, 9, 10, -1, 2]))
  print(count_rotations([1, 3, 8, 10]))
  print(count_rotations([1]))
  print(count_rotations([]))
