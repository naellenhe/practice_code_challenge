"""Split a string by splitter and return list of splits.

This should work like the built-in Python .split() method [*].
YOU MAY NOT USE the .split() method in your solution!
YOU MAY NOT USE regular expressions in your solution!

For example:

    >>> split("i love balloonicorn", " ")
    ['i', 'love', 'balloonicorn']

    >>> split("that is which is that which is that", " that ")
    ['that is which is', 'which is that']

    >>> split("that is which is that which is that", "that")
    ['', ' is which is ', ' which is ', '']

    >>> split("hello world", "nope")
    ['hello world']

* Note: the actual Python split method has special behavior
  when it is not passed anything for the splitter -- you do
  not need to implement that.

"""


def split(astring, splitter):
    """Split a string by splitter and return list of splits."""

    span = len(splitter)
    result = []

    i = 0
    prev = 0
    while i <= len(astring):
        if astring[i: i+span] == splitter:
            result.append(astring[prev: i])
            prev = i + span
            i += span

        i += 1

    if prev <= len(astring):
        result.append(astring[prev:])

    return result


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. FINE SPLITTING!\n"
