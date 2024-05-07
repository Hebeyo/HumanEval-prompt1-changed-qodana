from typing import List, Optional
def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    longest = strings[0]
    for s in strings:
        if len(s) > len(longest):
            longest = s
    return longest
