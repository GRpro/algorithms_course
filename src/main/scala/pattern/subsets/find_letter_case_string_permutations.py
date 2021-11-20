from collections import deque


def find_letter_case_string_permutations(str):
    permutations = deque()
    permutations.append(list(str))

    for i in range(len(str)):

        size = len(permutations)

        for k in range(size):
            p = permutations.popleft()

            ch = p[i]
            if ch.isalpha():
                new_p = p.copy()
                new_p[i] = ch.lower()
                permutations.append(new_p)

                new_p = p.copy()
                new_p[i] = ch.upper()
                permutations.append(new_p)
            else:
                permutations.append(p)


    return list(map(lambda p: "".join(p), permutations))


if __name__ == '__main__':

    print("String permutations are: " +
          str(find_letter_case_string_permutations("ad52")))
    print("String permutations are: " +
          str(find_letter_case_string_permutations("ab7c")))

