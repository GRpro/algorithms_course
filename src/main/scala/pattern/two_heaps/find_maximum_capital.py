from heapq import *

# Given a set of investment projects with their respective profits,
# we need to find the most profitable projects. We are given an initial
# capital and are allowed to invest only in a fixed number of projects.
# Our goal is to choose projects that give us the maximum profit.
# Write a function that returns the maximum total capital after selecting the most profitable projects.
# We can start an investment project only when we have the required capital.
# Once a project is selected, we can assume that its profit has become our capital.
def find_maximum_capital(capital, profits, numberOfProjects, initialCapital):
    if len(capital) != len(profits):
        return -1

    min_heap = []
    max_heap = []

    for i in range(len(profits)):
        c = capital[i]
        p = profits[i]
        heappush(min_heap, (c, p))

    capital = initialCapital
    for i in range(numberOfProjects):
        while min_heap and min_heap[0][0] <= capital:
            c, p = heappop(min_heap)
            print(f"invest {c} earn {p}")
            heappush(max_heap, (-p, c))

        if not max_heap:
            break

        p, c = heappop(max_heap)

        capital += -p

    return capital


if __name__ == '__main__':

    print("Maximum capital: " +
          str(find_maximum_capital([0, 1, 2], [1, 2, 3], 2, 1)))
    print("Maximum capital: " +
          str(find_maximum_capital([0, 1, 2, 3], [1, 2, 3, 5], 3, 0)))
