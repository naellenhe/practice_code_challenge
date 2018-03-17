"""Count items in a list recursively.

For example:

        >>> count_recursively([])
        0

        >>> count_recursively([1, 2, 3])
        3

        >>> count_recursively([1, 2, 3, -1, 3])
        5

"""


def count_recursively(lst):
    """Return number of items in a list, using recursion."""

    if not lst:
        return 0

    count = 1
    return count + count_recursively(lst[1:])


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GO YOU!\n"
