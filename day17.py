from __future__ import print_function


def sum_to(containers, goal, values_in_goal=0):
    """
    Find all sets of containers which sum to goal, store the number of
    containers used to reach the goal in the sizes variable.
    """
    if len(containers) == 0:
        return 0

    first = containers[0]
    remain = containers[1:]

    if first > goal:
        with_first = 0
    elif first == goal:
        sizes.append(values_in_goal + 1)
        with_first = 1
    else:
        with_first = sum_to(remain, goal-first, values_in_goal + 1)

    return with_first + sum_to(remain, goal, values_in_goal)


# example
sizes = []
containers = [20, 15, 10, 5, 5]
print(sum_to(containers, 25))
print(sum(min(sizes) == size for size in sizes))

# input data
sizes = []
containers = [33, 14, 18, 20, 45, 35, 16, 35, 1, 13,
              18, 13, 50, 44, 48, 6, 24, 41, 30, 42]
print(sum_to(containers, 150))
print(sum(min(sizes) == size for size in sizes))
