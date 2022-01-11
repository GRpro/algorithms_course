# Given a binary matrix representing an image, we want to flip the image horizontally, then invert it.
def flip_and_invert_image(matrix):
    for r in matrix:
        sz = len(r)
        for i in range(int(sz / 2)):
            r[i], r[sz - i - 1] = r[sz - i - 1], r[i]

        for i in range(sz):
            r[i] = r[i] ^ 1

    return matrix


if __name__ == '__main__':
    print(flip_and_invert_image([[1, 0, 1], [1, 1, 1], [0, 1, 1]]))
    print(flip_and_invert_image([[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]))

