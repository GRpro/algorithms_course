from collections import deque


# Given a set of distinct numbers, find all of its permutations.
# Permutation is defined as the re-arranging of the elements of the set. For example, {1, 2, 3} has the following six permutations:
def find_permutations(nums):
    result = deque()
    result.append([])

    for n in nums:

        size = len(result)
        for _ in range(size):
            p = result.popleft()

            i = 0
            while i <= len(p):
                new_p = p.copy()
                new_p.insert(i, n)
                result.append(new_p)
                i += 1

    return result


if __name__ == '__main__':
    print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))
