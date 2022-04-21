#   Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.
"""
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
from utils.timer import timer


@timer
def brute_force_solution(s: str):
    max_items = 0
    for i in range(len(s)):
        tmp_set = set()
        for j in range(i, len(s)):
            if s[j] not in tmp_set:
                tmp_set.add(s[j])
            else:
                break
        max_items = max(max_items, len(tmp_set))
    return max_items


@timer
def sliding_window_solution(s: str):
    max_items = 0
    sliding_window = []
    record_character_index = {}
    for i in s:
        if i not in sliding_window:
            sliding_window.append(i)
            record_character_index[i] = len(sliding_window)
        else:
            remove_idx = record_character_index[i]
            sliding_window = sliding_window[remove_idx:]
            sliding_window.append(i)
            record_character_index = {v: idx for idx, v in enumerate(sliding_window, 1)}
        max_items = max(max_items, len(sliding_window))
    return max_items


def sliding_window_solution_v2(s: str):
    max_items = 0
    window = {}
    for i, v in enumerate(s):
        if v not in window:
            window[v] = i
        else:
            remove_idx = window[v]
            window = {v: i for v, i in window.items() if i > remove_idx}
            window[v] = i
        max_items = max(max_items, len(window))
    return max_items



@timer
def two_pointer(s: str):
    chars = [0] * 128
    left = right = 0
    max_items = 0
    while right < len(s):
        r = s[right]
        chars[ord(r)] += 1
        while chars[ord(r)] > 1:
            l = s[left]
            chars[ord(l)] -= 1
            left += 1
        max_items = max(max_items, right - left + 1)
        right += 1
    return max_items






    # chars = [0] * 128
    # left = right = 0
    # res = 0
    # while right < len(s):
    #     r = s[right]
    #     chars[ord(r)] += 1
    #     while chars[ord(r)] > 1:
    #         l = s[left]
    #         chars[ord(l)] -= 1
    #         left += 1
    #     res = max(res, right - left + 1)
    #     right += 1
    # return res




brute_force_solution(" ")
sliding_window_solution(" ")
two_pointer(" ")

brute_force_solution("abcabcbb")
sliding_window_solution("abcabcbb")
two_pointer("abcabcbb")

brute_force_solution("pwwkew")
sliding_window_solution("pwwkew")
two_pointer("pwwkew")

brute_force_solution("bpfbhmipx")
sliding_window_solution("bpfbhmipx")
two_pointer("bpfbhmipx")