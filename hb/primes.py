"""Return count number of prime numbers, starting at 2.

For example::

    >>> primes(0)
    []

    >>> primes(1)
    [2]

    >>> primes(2)
    [2, 3]

    >>> primes(5)
    [2, 3, 5, 7, 11]

    >>> print primes(15)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

"""


def primes(count):
    """Return count number of prime numbers, starting at 2."""

    if count == 0:
        return []

    result = [2]

    if count == 1:
        return result

    i = 3
    while len(result) < count:
        prime = True
        for prime_num in result:
            if i % prime_num == 0:
                prime = False
        if prime:
            result.append(i)
        # Go to next odd number
        i += 2

    return result


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT WORK!\n"
