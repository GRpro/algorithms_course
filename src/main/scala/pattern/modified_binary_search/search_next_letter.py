
# Given an array of lowercase letters sorted in ascending order,
# find the smallest letter in the given array greater than a given ‘key’.
#
# Assume the given array is a circular list, which means that the last letter is assumed
# to be connected with the first letter. This also means that the smallest letter in the given
# array is greater than the last letter of the array and is also the first letter of the array.
#
# Write a function to return the next letter of the given ‘key’.
def search_next_letter(letters, key):
    if len(letters) == 0:
        return None

    if key >= letters[len(letters) - 1] or key < letters[0]:
        return letters[0]

    lo = 0
    hi = len(letters) - 1
    while lo < hi:
        m = (lo + hi) // 2
        if key >= letters[m]:
            lo = m + 1
        else:  # key < letters[m]:
            hi = m
    return letters[lo]


if __name__ == '__main__':

    print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))
    print(search_next_letter(['a', 'c', 'f', 'm'], 'm'))
    print(search_next_letter(['b', 'm'], 'a'))
