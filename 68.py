def pluck(arr):
    if not arr:
        return []
    even = [x for x in arr if x % 2 == 0]
    if not even:
        return []
    smallest = min(even)
    return [smallest, arr.index(smallest)]
