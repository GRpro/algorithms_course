from __future__ import print_function
from heapq import *


# For ‘K’ employees, we are given a list of intervals representing the working hours of each employee.
# Our goal is to find out if there is a free interval that is common to all employees.
# You can assume that each list of employee working hours is sorted on the start time.
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


class EmployeeInterval:

    def __init__(self, interval, employeeIndex, intervalIndex):
        self.interval = interval  # interval representing employee's working hours
        # index of the list containing working hours of this employee
        self.employeeIndex = employeeIndex
        self.intervalIndex = intervalIndex  # index of the interval in the employee list

    def __lt__(self, other):
        # min heap based on meeting.end
        return self.interval.start < other.interval.start


def find_employee_free_time(schedule):
    if schedule is None:
        return []

    result = []

    minheap = []
    for i in range(len(schedule)):
        heappush(minheap, EmployeeInterval(schedule[i][0], i, 0))

    previous_interval = minheap[0].interval
    while minheap:
        queue_top = heappop(minheap)

        # if previous_interval is not overlapping with the next interval, insert a free interval
        if previous_interval.end < queue_top.interval.start:
            result.append(Interval(previous_interval.end,
                                   queue_top.interval.start))
            previous_interval = queue_top.interval
        else:  # overlapping intervals, update the previous_interval if needed
            if previous_interval.end < queue_top.interval.end:
                previous_interval = queue_top.interval

                # if there are more intervals available for the same employee, add their next interval
        employeeSchedule = schedule[queue_top.employeeIndex]
        if len(employeeSchedule) > queue_top.intervalIndex + 1:
            heappush(minheap, EmployeeInterval(employeeSchedule[queue_top.intervalIndex + 1], queue_top.employeeIndex,
                                               queue_top.intervalIndex + 1))

    return result


if __name__ == '__main__':

    input = [[Interval(1, 3), Interval(5, 6)], [
        Interval(2, 3), Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3), Interval(9, 12)], [
        Interval(2, 4)], [Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3)], [
        Interval(2, 4)], [Interval(3, 5), Interval(7, 9)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()