def max_element(l: list):
    if not l:
        return None
    m = l[0]
    for e in l:
        if e > m:
            m = e
    return m
