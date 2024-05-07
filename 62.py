def derivative(xs: list):
    ret = []
    for i, x in enumerate(xs):
        if i == 0:
            continue
        ret.append(i * x)
    return ret
