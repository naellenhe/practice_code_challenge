"""Leaping lemur.

Calculate the fewest number of jumps the lemur needs to
jump to the last tree. The lemur can jump 1 or 2 branches.
It cannot use deadly branch (1 in the list).

    >>> lemur([0])
    0

    >>> lemur([0, 0])
    1

    >>> lemur([0, 0, 0])
    1

    >>> lemur([0, 1, 0])
    1

    >>> lemur([0, 0, 1, 0])
    2

    >>> lemur([0, 0, 0, 0, 1, 0, 0, 1, 0])
    5
"""

#My approach
# def lemur(branches):
#     """Return number of jumps needed."""

#     assert branches[0] == 0, "First branch must be alive"
#     assert branches[-1] == 0, "Last branch must be alive"

#     dead_branches = []
#     jumps = 0
#     for i, branch in enumerate(branches):
#         if branch == 1:
#             previous_dead_branches = 0 if not dead_branches else dead_branches[-1]
#             step = i - previous_dead_branches - 1
#             jumps += ((step // 2) + (step % 2))
#             dead_branches.append(i)
#     if 1 not in branches:
#         step = len(branches) - 1
#         jumps += ((step // 2) + (step % 2))
#     return jumps + len(dead_branches)


def lemur(branches):
    """Return number of jumps needed."""

    assert branches[0] == 0, "First branch must be alive"
    assert branches[-1] == 0, "Last branch must be alive"

    # START SOLUTION

    at = 0
    n_jumps = 0

    while at < len(branches) - 1:
        at += 2
        if at >= len(branches) or branches[at] == 1:
            # We can jump this far, so only jump 1
            at -= 1
        n_jumps += 1

    return n_jumps

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. NICE JUMPING!\n"
