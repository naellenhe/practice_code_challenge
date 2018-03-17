"""Find the most frequent num(s) in nums.

Return the set of nums that are the mode::

    >>> mode([1]) == {1}
    True

    >>> mode([1, 2, 2, 2]) == {2}
    True

If there is a tie, return all::

    >>> mode([1, 1, 2, 2]) == {1, 2}
    True
"""


def mode(nums):
    """Find the most frequent num(s) in nums."""

    while nums:
        distinct_nums = set(nums)
        if len(distinct_nums) == 1:
            return distinct_nums
        else:
            for num in distinct_nums:
                nums.remove(num)
    return distinct_nums


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. HOORAY!\n"
