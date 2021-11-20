# Given a set of numbers that might contain duplicates, find all of its distinct subsets.
def find_subsets(nums):
    subsets = []
    subsets.append([])
    used = set()

    for n in nums:

        size = len(subsets)
        for i in range(size):
            subset = subsets[i]
            new_subset = subset.copy()
            new_subset.append(n)

            if str(new_subset) not in used:
                used.add(str(new_subset))
                subsets.append(new_subset)

    return subsets


if __name__ == '__main__':

    print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))

