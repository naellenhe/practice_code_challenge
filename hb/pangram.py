"""Given a string, return True if it is a pangram, False otherwise.

For example::

    >>> is_pangram("The quick brown fox jumps over the lazy dog!")
    True

    >>> is_pangram("I love cats, but not mice")
    False
"""


def is_pangram(sentence):
    """Given a string, return True if it is a pangram, False otherwise."""

    chars_set = set([char.lower() for char in sentence if char.isalpha()])
    # print chars_set
    return len(chars_set) == 26

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSE    D. YAY!\n"
