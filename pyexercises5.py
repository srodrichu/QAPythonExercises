# Given three ints, a b c, one of them is small, one is medium and one is large.
# Return the boolean True if the three values are evenly spaced, so the
# difference between small and medium is the same as the difference between
# medium and large.
# Do not assume the ints will come to you in a reasonable order.
# <EXAMPLES>
# seven(2, 4, 6) → True
# seven(4, 6, 2) → True
# seven(4, 6, 3) → False
# seven(4, 60, 9) → False
# <HINT>
# There is a function for lists called sort.


from operator import truediv


def seven(n1, n2, n3):

    sort_ints = [n1, n2, n3]

    sort_ints.sort()

    if (sort_ints[1] - sort_ints[0]) == (sort_ints[2] - sort_ints[1]):
        return True
    return False


print(seven(4, 6, 2))
