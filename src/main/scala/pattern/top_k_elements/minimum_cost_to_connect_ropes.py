from heapq import *

# Given ‘N’ ropes with different lengths, we need to connect these ropes into one big rope with minimum cost.
# The cost of connecting two ropes is equal to the sum of their lengths.
def minimum_cost_to_connect_ropes(ropeLengths):
    min_heap = []

    for r in ropeLengths:
        heappush(min_heap, r)

    s = 0
    while len(min_heap) > 1:
        a = heappop(min_heap)
        b = heappop(min_heap)
        print(f"{a} and {b}")

        s += a + b
        heappush(min_heap, a + b)
    return s


if __name__ == '__main__':

    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([1, 3, 11, 5])))
    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([3, 4, 5, 6])))
    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([1, 3, 11, 5, 2])))
