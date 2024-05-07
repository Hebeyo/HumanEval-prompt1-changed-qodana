def pairs_sum_to_zero(l):
    l = list(set(l))
    n = len(l)
    for i in range(n):
        for j in range(i + 1, n):
            if l[i] + l[j] == 0:
                return True
    return False
