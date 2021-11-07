# Any number will be called a happy number if, after repeatedly replacing it with a number equal to the sum of the square of all of its digits, leads us to number ‘1’. All other (not-happy) numbers will never reach ‘1’. Instead, they will be stuck in a cycle of numbers which does not include ‘1’.
def find_happy_number(num):
    def next_number(num):
        s = 0
        for ch in str(num):
            n = int(ch)
            s += n ** 2
        return s

    slow = num
    fast = num
    while next_number(slow) != 1 and next_number(next_number(fast)) != 1:
        slow = next_number(slow)
        fast = next_number(next_number(fast))
        if slow == fast:
            return False
    return True


if __name__ == '__main__':

    print(find_happy_number(23))
    print(find_happy_number(12))

