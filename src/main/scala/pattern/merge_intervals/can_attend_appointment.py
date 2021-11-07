# Given an array of intervals representing ‘N’ appointments,
# find out if a person can attend all the appointments (no intersection).
def can_attend_all_appointments(intervals):
    intervals.sort(key=lambda x:x[0])

    lnt = len(intervals)
    if lnt < 2:
        return True
    else:
        last_y = intervals[0][1]
    for i in range(1, len(intervals)):
        int = intervals[i]
        if int[0] < last_y:
            return False
        last_y = int[1]
    return True


if __name__ == '__main__':

    print("Can attend all appointments: " + str(can_attend_all_appointments([[1, 4], [2, 5], [7, 9]])))
    print("Can attend all appointments: " + str(can_attend_all_appointments([[6, 7], [2, 4], [8, 12]])))
    print("Can attend all appointments: " + str(can_attend_all_appointments([[4, 5], [2, 3], [3, 6]])))
