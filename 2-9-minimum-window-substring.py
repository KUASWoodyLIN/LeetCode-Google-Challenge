from collections import defaultdict
from utils.timer import timer


@timer
def solution(s: str, t: str) -> str:
    chr_idx_search = defaultdict()
    for i, c in enumerate(s):
        chr_idx_search[c].append(i)

    # for c in t:


@timer
def sliding_window(s: str, t: str) -> str:
    left = right = 0
    min_window_str = ""
    target_t_num = defaultdict(int)
    check_t_num = defaultdict(int)
    for c in t:
        target_t_num[c] += 1

    while right <= len(s)-1:
        # check is right point in [t]
        if s[right] in t:
            check_t_num[s[right]] += 1
        # check is window full
        right += 1
        if all([target_t_num[c] <= check_t_num[c] for c in target_t_num.keys()]):
            if len(s[left:right]) < len(min_window_str) or len(min_window_str) == 0:
                min_window_str = s[left:right]
            # move left
            while left <= right-1:
                # check is left point in [t]
                if s[left] in t:
                    check_t_num[s[left]] -= 1
                    if target_t_num[s[left]] > check_t_num[s[left]]:
                        left += 1
                        break
                left += 1
                if len(s[left:right]) < len(min_window_str):
                    min_window_str = s[left:right]

    return min_window_str




sliding_window("ADOBECODEBANC", "ABC")      # Output: "BANC"
sliding_window("a", "a")      # Output: "a"
sliding_window("a", "b")      # Output: ""
sliding_window("abc", "b")      # Output: "b"