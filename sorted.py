def some_sort(arr: list, reverse: bool = False):

    clist = arr[:]

    if len(arr) == 0:
        return clist

    felem = clist[0]

    lower_list = [e for e in clist if e < felem]
    hight_list = [e for e in clist if e > felem]

    if not reverse:
        return some_sort(lower_list) + [e for e in clist if e == felem] + some_sort(hight_list)
    else:
        return some_sort(hight_list, reverse=True) + [e for e in clist if e == felem] + some_sort(lower_list, reverse=True)


print(some_sort([20, 0, -10, 2, 56, 1000]))
