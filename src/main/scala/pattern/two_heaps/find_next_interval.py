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
    max_start_heap = []
    max_end_heap = []

    n = len(intervals)
    result = [0] * n

    for end_index in range(n):
        heappush(max_start_heap, (-intervals[end_index].start, end_index))
        heappush(max_end_heap, (-intervals[end_index].end, end_index))

    # go through all the intervals to find each interval's next interval
    while max_end_heap:
        # let's find the next interval of the interval which has the highest 'end'
        top_end, end_index = heappop(max_end_heap)
        result[end_index] = -1  # defaults to - 1
        if -max_start_heap[0][0] >= -top_end:
            top_start, start_index = heappop(max_start_heap)
            # find the the interval that has the closest 'start'
            while max_start_heap and -max_start_heap[0][0] >= -top_end:
                top_start, start_index = heappop(max_start_heap)
            result[end_index] = start_index
            # put the interval back as it could be the next interval of other intervals
            heappush(max_start_heap, (top_start, start_index))

    return result


if __name__ == '__main__':

    result = find_next_interval(
        [Interval(2, 3), Interval(3, 4), Interval(5, 6)])
    print("Next interval indices are: " + str(result))

    result = find_next_interval(
        [Interval(3, 4), Interval(1, 5), Interval(4, 6)])
    print("Next interval indices are: " + str(result))

