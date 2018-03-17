"""Given list (haystack), return index (0-based) of needle in the list.

    Return None if needle is not in haystack.

    Do this with recursion. You MAY NOT USE A `for` OR `while` LOOP.

For example:

    >>> recursive_index(5, [1, 3, 5, 2, 4])
    2

    >>> recursive_index("hey", ["hey", "there", "you"])
    0

    >>> recursive_index("you", ["hey", "there", "you"])
    2

    >>> recursive_index("zork", ["foo", "bar", "baz"]) is None
    True

"""


def recursive_index(needle, haystack):
    """Given list (haystack), return index (0-based) of needle in the list.

    Return None if needle is not in haystack.

    Do this with recursion. You MAY NOT USE A `for` OR `while` LOOP.
    """

    # if not haystack:
    #     return None
    # elif needle == haystack[0]:
    #     return 0

    # if recursive_index(needle, haystack[1:]) is not None:
    #     return 1 + recursive_index(needle, haystack[1:])
    # #if not found
    # else:
    #     return None

    def _recursive_index(needle, haystack, current_index):
        # Check if not found
        if current_index == len(haystack):
            return None
        if needle == haystack[current_index]:
            return current_index
        else:
            return _recursive_index(needle, haystack, current_index + 1)

    return _recursive_index(needle, haystack, 0)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GO GO GO!\n"
