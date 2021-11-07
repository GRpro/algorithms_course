# Given a list of non-overlapping intervals sorted by their start time,
# insert a given interval at the correct position and merge all necessary
# intervals to produce a list that has only mutually exclusive intervals.
def insert(intervals, new_interval):
    merged = []

    if len(intervals) == 0:
        return [new_interval]

    start = new_interval[0]
    end = new_interval[1]

    i = 0
    while i < len(intervals):
        if intervals[i][1] < start:
            merged.append(intervals[i])
            i += 1
        else:
            break

    if i == len(intervals):
        # no intersection
        merged.append([start, end])
    else:

        if intervals[i][0] < end and intervals[i][1] > start:
            # intersects
            s = min(intervals[i][0], start)
            e = max(intervals[i][1], end)
        else:
            s = intervals[i][0]
            e = intervals[i][1]
            
        while i < len(intervals):
            x = intervals[i]
            if x[0] <= e:
                # intersects
                e = max(e, x[1])
            else:
                merged.append([s, e])
                s = x[0]
                e = x[1]
            i += 1
        merged.append([s, e])

    return merged


if __name__ == '__main__':

    print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
    print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
    print("Intervals after inserting the new interval: " + str(insert([[2, 3], [5, 7]], [1, 4])))

