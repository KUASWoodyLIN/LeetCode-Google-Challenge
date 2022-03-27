"""
Input: s = "abcd", indices = [0, 2], sources = ["ab","ec"], targets = ["eee","ffff"]
Output: "eeecd"
Explanation:
"ab" occurs at index 0 in s, so we replace it with "eee".
"ec" does not occur at index 2 in s, so we do nothing.
"""

from utils.timer import timer


@timer
def solution1(s: str, indices: list, sources: list, targets: list) -> str:
    tmp = [(i, s, t) for i, s, t in sorted(zip(indices, sources, targets), key=lambda x:x[0])]
    indices = [t[0] for t in tmp]
    sources = [t[1] for t in tmp]
    targets = [t[2] for t in tmp]

    indices_start_end = [(i, i+len(s)) for i, s in zip(indices, sources)]
    result = []

    if (indices_start_end[0][1] <= indices_start_end[1][0]) and sources[0] == s[indices_start_end[0][0]:indices_start_end[0][1]]:
        result.append((s[0:indices_start_end[0][0]]))
        result.append(targets[0])
    else:
        result.append((s[0:indices_start_end[0][1]]))
        # result.append('')

    for i in range(1, len(indices)-1):
        if (indices_start_end[i][0] >= indices_start_end[i-1][1]) and \
           (indices_start_end[i][1] <= indices_start_end[i+1][0]) and \
           (sources[i] == s[indices_start_end[i][0]:indices_start_end[i][1]]):
            result.append((s[indices_start_end[i-1][1]:indices_start_end[i][0]]))
            result.append(targets[i])
        else:
            result.append((s[indices_start_end[i - 1][1]:indices_start_end[i][1]]))
            # result.append('')
    end = len(indices)-1
    if (indices_start_end[end][0] >= indices_start_end[end-1][1]) and \
       (sources[end] == s[indices_start_end[end][0]:indices_start_end[end][1]]):
        result.append((s[indices_start_end[end-1][1]:indices_start_end[end][0]]))
        result.append(targets[end])
        result.append((s[indices_start_end[end][1]:]))
    else:
        # result.append('')
        result.append((s[indices_start_end[end-1][1]:]))
    return ''.join(result)


@timer
def solution2(s: str, indices: list, sources: list, targets: list) -> str:
    tmp_dict = {}
    for idx, src, tgt in zip(indices, sources, targets):
        if s[idx:idx+len(src)] == src:
            tmp_dict[idx] = (len(src), tgt)
    i = 0
    new_str = ""
    while i < len(s):
        if i in tmp_dict:
            new_str += tmp_dict[i][1]
            i += tmp_dict[i][0]
        else:
            new_str += s[i]
            i += 1
    return new_str



        # solution1("abc", [0, 1], ["ab", "bc"], ["eee", "fff"])      # Output: abc
# solution1("abcd", [0, 2], ["a", "cd"], ["eee", "ffff"])      # Output: "eeebffff"
# solution1("abcd", [0, 2], ["ab", "ec"], ["eee", "ffff"])      # Output: "eeecd"
# solution1("vmokgggqzp", [3,5,1], ["kg","ggq","mo"], ["s","so","bfr"])       # "vbfrssozp"


solution2("abc", [0, 1], ["ab", "bc"], ["eee", "fff"])      # Output: abc
solution2("abcd", [0, 2], ["a", "cd"], ["eee", "ffff"])      # Output: "eeebffff"
solution2("abcd", [0, 2], ["ab", "ec"], ["eee", "ffff"])      # Output: "eeecd"
solution2("vmokgggqzp", [3,5,1], ["kg","ggq","mo"], ["s","so","bfr"])       # "vbfrssozp"