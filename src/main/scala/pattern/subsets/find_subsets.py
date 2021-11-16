def find_subsets(nums):
    subsets = []
    subsets.append([])
    for k in nums:
        n = len(subsets)
        for i in range(n):
            subset = subsets[i]
            new_subset = subset.copy()
            new_subset.append(k)
            subsets.append(new_subset)
    return subsets


if __name__ == '__main__':
    print("Here is the list of subsets: " + str(find_subsets([1, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))
