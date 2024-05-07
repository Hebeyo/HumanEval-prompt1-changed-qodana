from typing import List, Tuple
def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    return min([(numbers[i], numbers[i+1]) for i in range(len(numbers)-1)], key=lambda x: x[1] - x[0])
