from __future__ import print_function


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


# Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.
def merge(intervals):
    if len(intervals) == 0:
        return []

    intervals.sort(key=lambda i: i.start)

    merged = []
    start = intervals[0].start
    end = intervals[0].end
    for i in range(1, len(intervals)):
        x = intervals[i]
        if x.start <= end:
            # intersects
            end = max(end, x.end)
        else:
            merged.append(Interval(start, end))
            start = x.start
            end = x.end

    merged.append(Interval(start, end))
    return merged


if __name__ == '__main__':

    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(0,1), Interval(2,4), Interval(3,6), Interval(4,5)]):
        i.print_interval()
    print()
