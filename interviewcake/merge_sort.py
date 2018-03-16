def merge_lists(lst1, lst2):
    """Use merge to sort lists.
        >>> list1 = [3, 4, 6]
        >>> list2 = [1, 5]
        >>> print merge_lists(list1, list2)
        [1, 3, 4, 5, 6]

        >>> list1     = [3, 4, 6, 10, 11, 12, 15, 20, 20]
        >>> list2 = [1, 5, 8, 12, 14, 19, 20]
        >>> print merge_lists(list1, list2)
        [1, 3, 4, 5, 6, 8, 10, 11, 12, 12, 14, 15, 19, 20, 20, 20]

    """
    result = []
    while lst1 and lst2:
        if lst1[0] < lst2[0]:
            result.append(lst1.pop(0))
        else:
            result.append(lst2.pop(0))
    if not lst1:
        result.extend(lst2)
    if not lst2:
        result.extend(lst1)

    return result


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. NICE STACKING!\n"