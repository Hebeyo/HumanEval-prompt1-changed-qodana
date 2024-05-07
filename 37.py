def sort_even(l: list):
    evens = [l[i] for i in range(0, len(l), 2)]
    odds = [l[i] for i in range(1, len(l), 2)]
    evens.sort()
    ans = []
    for e, o in zip(evens, odds):
        ans.extend([e, o])
    if len(evens) > len(odds):
        ans.append(evens[-1])
    return ans
