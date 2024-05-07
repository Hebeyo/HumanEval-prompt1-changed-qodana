from typing import List
def string_xor(a: str, b: str) -> str:
    result = []
    for i in range(len(a)):
        if a[i] != b[i]:
            result.append('1')
        else:
            result.append('0')
    return ''.join(result)
