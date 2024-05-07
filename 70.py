def strange_sort_list(lst):
    res = []
    switch = True
    while lst:
        if switch:
            res.append(min(lst))
            lst.remove(min(lst))
            switch = False
        else:
            res.append(max(lst))
            lst.remove(max(lst))
            switch = True
    return res
