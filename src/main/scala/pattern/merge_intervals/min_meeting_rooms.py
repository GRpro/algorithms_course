from heapq import *


class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end


# Given a list of intervals representing the start and end time of ‘N’ meetings,
# find the minimum number of rooms required to hold all the meetings.
def min_meeting_rooms(meetings):

    meetings.sort(key=lambda x: x.start)

    minRooms = 0
    minHeap = []
    for meeting in meetings:
        # remove all the meetings that have ended
        while len(minHeap) > 0 and meeting.start >= minHeap[0]:
            heappop(minHeap)

        # add the current meeting into min_heap
        heappush(minHeap, meeting.end)

        # all active meetings are in the min_heap, so we need rooms for all of them.
        minRooms = max(minRooms, len(minHeap))

    return minRooms


def min_meeting_rooms1(meetings):
    int = {}
    for m in meetings:
        for i in range(m.start, m.end):
            v = int.get(i)
            if v is None:
                int[i] = 1
            else:
                int[i] = v + 1

    min = 0
    for v in int.values():
        min = max(min, v)
    return min


if __name__ == '__main__':
    print("Minimum meeting rooms required: " + str(min_meeting_rooms(
        [Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)])))
    print("Minimum meeting rooms required: " +
          str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 5), Meeting(7, 9)])))
    print("Minimum meeting rooms required: " +
          str(min_meeting_rooms([Meeting(6, 7), Meeting(2, 4), Meeting(8, 12)])))
    print("Minimum meeting rooms required: " +
          str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 3), Meeting(3, 6)])))
    print("Minimum meeting rooms required: " + str(min_meeting_rooms(
        [Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)])))