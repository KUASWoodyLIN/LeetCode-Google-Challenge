from utils.timer import timer
import itertools


@timer
def solution1(s: str, t: str) -> bool:
    tmp1 = []
    for i in range(len(s)):
        if s[i] == '#':
            if tmp1:
                tmp1.pop()
        else:
            tmp1.append(s[i])
    tmp2 = []
    for i in range(len(t)):
        if t[i] == '#':
            if tmp2:
                tmp2.pop()
        else:
            tmp2.append(t[i])
    return tmp1 == tmp2


@timer
def solution2(s: str, t: str) -> bool:
    def F(S):
        skip = 0
        for x in reversed(S):
            if x == '#':
                skip += 1
            elif skip:
                skip -= 1
            else:
                yield x

    return all(x == y for x, y in itertools.zip_longest(F(s), F(t)))

# solution1("ab##", "c#d#")
# solution1("xywrrmp","xywrrmu#p")


solution2("ab##", "c#d#")
solution2("xywrrmp","xywrrmu#p")
for i in range(10):
    continue