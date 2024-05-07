def f(n):
    result = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            factorial = 1
            for j in range(1, i + 1):
                factorial *= j
            result.append(factorial)
        else:
            summation = 0
            for j in range(1, i + 1):
                summation += j
            result.append(summation)
    return result
