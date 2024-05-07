def is_sorted(lst):
    return all(lst[i-1] <= lst[i] for i in range(1, len(lst))) and all(lst.count(i) < 3 for i in lst)
