from collections import deque


# Given an expression containing digits and operations (+, -, *), find all possible ways in which
# the expression can be evaluated by grouping the numbers and operators using parentheses.
def diff_ways_to_evaluate_expression(input):
    result = deque()
    result.append(list(input))

    op = {"+", "-", "*"}

    ex_size = len(result[0])

    while ex_size > 1:
        s = len(result)
        for _ in range(s):
            ex = result.popleft()

            i = 0
            while i < len(ex):
                if ex[i] in op:
                    if ex[i] == "+":
                        new_ex = ex[:i - 1].copy()
                        new_ex.append(int(ex[i - 1]) + int(ex[i + 1]))
                        new_ex.extend(ex[i + 2:].copy())
                        result.append(new_ex)
                        ex_size = len(new_ex)
                    elif ex[i] == "-":
                        new_ex = ex[:i - 1].copy()
                        new_ex.append(int(ex[i - 1]) - int(ex[i + 1]))
                        new_ex.extend(ex[i + 2:].copy())
                        result.append(new_ex)
                        ex_size = len(new_ex)
                    else:  # s[i] == "*"
                        new_ex = ex[:i - 1].copy()
                        new_ex.append(int(ex[i - 1]) * int(ex[i + 1]))
                        new_ex.extend(ex[i + 2:].copy())
                        result.append(new_ex)
                        ex_size = len(new_ex)
                i += 1

    return list(set(map(lambda e: e[0], result)))


if __name__ == '__main__':

    print("Expression evaluations: " +
          str(diff_ways_to_evaluate_expression("1+2*3")))

    print("Expression evaluations: " +
          str(diff_ways_to_evaluate_expression("2*3-4-5")))

