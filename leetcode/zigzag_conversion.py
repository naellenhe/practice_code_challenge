"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
of rows like this:

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);


    >>> string_convert("PAYPALISHIRING", 3)
    'PAHNAPLSIIGYIR'

    >>> string_convert("PAYPALISHIRING", 4)
    'PINALSIGYAHRPI'
"""


def string_convert(s, num):

    if len(s) <= 1 or num <= 1:
        return s

    else:
        chars = [''] * num

        # one cycle is : num + (num -2)
        cycle = num + (num - 2)

        d = {a: a if a < num else (num-2)-a for a in range(cycle)}

        for i, char in enumerate(s):
            loc = i % cycle
            chars[d[loc]] += char

        return ''.join(chars)


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED!\n"
