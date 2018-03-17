"""How many days are there in a month?

Given a string with a month and a year (separated by a space),
returns the number of days in that month.

For example::

    >>> for i in range(1, 13):
    ...     date = str(i) + " 2016"
    ...     print "%s has %s days." % (date, days_in_month(date))
    1 2016 has 31 days.
    2 2016 has 29 days.
    3 2016 has 31 days.
    4 2016 has 30 days.
    5 2016 has 31 days.
    6 2016 has 30 days.
    7 2016 has 31 days.
    8 2016 has 31 days.
    9 2016 has 30 days.
    10 2016 has 31 days.
    11 2016 has 30 days.
    12 2016 has 31 days.

    >>> days_in_month("02 2015")
    28
"""


def is_leap_year(year):
    """Is this year a leap year?

    Every 4 years is a leap year::

        >>> is_leap_year(1904)
        True

    Except every hundred years::

        >>> is_leap_year(1900)
        False

    Except-except every 400::

        >>> is_leap_year(2000)
        True
    """

    if year % 400 == 0:
        return True

    if year % 100 == 0:
        return False

    if year % 4 == 0:
        return True


def days_in_month(date):
    """How many days are there in a month?

    input: "02 2015" (string)
    output: 28 (int)
    """

    m, y = map(lambda x: int(x), date.split())
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(y):
        days[1] = 29

    return days[m-1]


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. W00T!\n"
