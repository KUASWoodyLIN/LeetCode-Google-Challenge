"""
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "{[]}"
Output: true
"""
from utils.timer import timer


@timer
def solution1(s: str) -> bool:
    # if len(s) % 2 == 1:
    #     return False
    tmp = []
    for c in s:
        if c in ["(", "[", "{"]:
            tmp.append(c)
        elif tmp:
            get_c = tmp.pop()
            if get_c == "(" and c == ")":
                continue
            elif get_c == "[" and c == "]":
                continue
            elif get_c == "{" and c == "}":
                continue
            return False
        else:
            return False
    if len(tmp) == 0:
        return True
    else:
        return False


@timer
def solution2(s: str) -> bool:
    mapping = {")": "(", "]": "[", "}": "{"}
    tmp = []
    for c in s:
        if c in mapping:
            get_c = tmp.pop() if tmp else ''
            if mapping.get(c, None) != get_c:
                return False
        else:
            tmp.append(c)
    if len(tmp) == 0:
        return True
    else:
        return False


solution1("()")
solution1("()[]{}")
solution1("(]")
solution1("{[]}")
solution1("((")
solution1("(")
solution1(")")