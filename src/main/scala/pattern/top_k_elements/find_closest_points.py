from heapq import *
import math
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_point(self):
        print("[" + str(self.x) + ", " + str(self.y) + "] ", end='')

    def distance_from_origin(self):
        # ignoring sqrt to calculate the distance
        return (self.x * self.x) + (self.y * self.y)

    # used for max-heap
    def __lt__(self, other):
        return self.distance_from_origin() > other.distance_from_origin()


def find_closest_points(points, k):
    result = []

    for p in points:
        if len(result) >= k:

            if result[0].distance_from_origin() > p.distance_from_origin():
                heappop(result)
                heappush(result, p)

        else:
            heappush(result, p)
    return result


if __name__ == '__main__':

    result = find_closest_points([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
    print("Here are the k points closest the origin: ", end='')
    for point in result:
        point.print_point()

