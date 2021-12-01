from collections import deque


def generate_valid_parentheses(num):
    result = []

    def gen(cur, left_open, left_closed):
        if left_closed == 0:
            result.append(cur)
            return

        if left_open == 0:
            gen(cur + ")", left_open, left_closed - 1)
        else:
            gen(cur + "(", left_open - 1, left_closed)
            if left_open < left_closed:
                gen(cur + ")", left_open, left_closed - 1)

    gen("", num, num)

    return result


def generate_valid_parentheses_bfs(num):
    result = deque()
    result.append(("", 0, 0))

    cnt = 2 * num
    while cnt > 0:
        size = len(result)
        for _ in range(size):
            (s, used_open, used_closed) = result.popleft()
            if used_open < num:
                result.append((s + "(", used_open + 1, used_closed))

            if used_open > used_closed:
                result.append((s + ")", used_open, used_closed + 1))
        cnt -= 1

    return list(map(lambda tpl: tpl[0], result))


if __name__ == '__main__':

    print("All combinations of balanced parentheses are: " +
          str(generate_valid_parentheses_bfs(2)))
    print("All combinations of balanced parentheses are: " +
          str(generate_valid_parentheses_bfs(3)))

