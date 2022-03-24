# Longest Substring with At Most Two Distinct Characters
# https://leetcode.com/explore/interview/card/google/59/array-and-strings/3054/
# Given a string s, return the length of the longest substring that contains at most two distinct characters.
"""
Example 1:

Input: s = "eceba"
Output: 3
Explanation: The substring is "ece" which its length is 3.
"""

"""
Example 2:

Input: s = "ccaabbb"
Output: 5
Explanation: The substring is "aabbb" which its length is 5.

s consists of English letters.
"""
from utils.timer import timer
from collections import defaultdict


# @timer
# def two_pointer(s: str) -> int:
#     max_size = left = right = 0
#     chars_dict = defaultdict(list)
#     while right < len(s):
#         chars_dict[s[right]].append(right)
#         while len(chars_dict) > 2:
#             indices = chars_dict.pop(s[right-1])
#             left = indices[-1] + 1
#         if right - left + 1 > max_size:
#             max_size = right - left + 1
#         right += 1
#     return max_size
@timer
def two_pointer(s: str) -> int:
    max_size = left = right = 0
    continue_indices = defaultdict(list)
    while right < len(s):

        if s[right] in continue_indices:
            if continue_indices[s[right]][-1] + 1 == right:
                continue_indices[s[right]].append(right)
            else:
                continue_indices[s[right]] = [right]
        else:
            continue_indices[s[right]] = [right]

        while len(continue_indices) > 2:
            indices = continue_indices[s[right - 1]]
            left = indices[0]
            continue_indices.pop(s[left-1])

        if right - left + 1 > max_size:
            max_size = right - left + 1
        right += 1
    return max_size


@timer
def sliding_window(s: str) -> int:

    return 0



two_pointer("eceba")
two_pointer("ccaabbb")
two_pointer("abaccc")