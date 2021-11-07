import math


# Given two lists of intervals, find the intersection of these two lists.
# Each list consists of disjoint intervals sorted on their start time.
def merge(intervals_a, intervals_b):
    result = []
    
    i = 0
    j = 0

    had_intersection = False
    while i < len(intervals_a) and j < len(intervals_b):
        xa = intervals_a[i][0]
        ya = intervals_a[i][1]
        
        xb = intervals_b[j][0]
        yb = intervals_b[j][1]

        if not (yb <= xa or xb >= ya):
            # intersection
            result.append([max(xa, xb), min(ya, yb)])

            if ya < yb:
                i += 1
            else:   # yb <= ya
                j += 1

        else:
            # no intersection
            if yb <= xa:
                j += 1
            elif xb >= ya:
                i += 1

    return result


if __name__ == '__main__':

    print("Intervals Intersection: " + str(merge(
        [[1, 3], [5, 6], [7, 9]],
        [[2, 3], [5, 7]])))
    print("Intervals Intersection: " + str(merge(
        [[1, 3], [5, 7], [9, 12]],
        [[5, 10]])))
    print("Intervals Intersection: " + str(merge(
        [[1, 3], [5, 7], [9, 12]],
        [[2, 6]])))
