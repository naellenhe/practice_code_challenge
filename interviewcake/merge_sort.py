def merge_lists(lst1, lst2):
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

my_list = [3, 4, 6, 10, 11, 12, 15, 20, 20]
alices_list = [1, 5, 8, 12, 14, 19, 20]

print merge_lists(my_list, alices_list)
