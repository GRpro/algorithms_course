from heapq import *
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

# Given an array of intervals, find the next interval of each interval. In a list of intervals,
# for an interval ‘i’ its next interval ‘j’ will have the smallest ‘start’ greater than or equal to the ‘end’ of ‘i’.

# Write a function to return an array containing indices of the next interval of each input interval.
# If there is no next interval of a given interval, return -1.
# It is given that none of the intervals have the same start point.
def find_next_interval(intervals):
    min_heap = []
    for i in range(len(intervals)):
        int = intervals[i]
        heappush(min_heap, (int.start, i))
    result = []

    return result


if __name__ == '__main__':

    result = find_next_interval(
        [Interval(2, 3), Interval(3, 4), Interval(5, 6)])
    print("Next interval indices are: " + str(result))

    result = find_next_interval(
        [Interval(3, 4), Interval(1, 5), Interval(4, 6)])
    print("Next interval indices are: " + str(result))

