""""
Write a function reverse_words() that takes a message as a list of characters
and reverses the order of the words in-place.
When writing your function, assume the message contains
only letters and spaces, and all words are separated by one space.


    >>> message = "the sky is blue"
    >>> reverse_words(message)
    'blue is sky the'

"""


def reverse_words(s):
    """
    input: words
    output: reversed words

    """

    s = s.split()
    for i in range(len(s)/2):
        (s[i], s[-1-i]) = (s[-1-i], s[i])

    return ' '.join(s)


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED!\n"
