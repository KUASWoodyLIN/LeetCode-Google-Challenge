"""
  Expressive Words
Sometimes people repeat letters to represent extra feeling. For example:

 - "hello" -> "heeellooo"
 - "hi" -> "hiiii"
In these strings like "heeellooo", we have groups of adjacent letters that are all the same: "h", "eee", "ll", "ooo".
You are given a string s and an array of query strings words. A query word is stretchy if it can be made to be equal to s by any number of applications of the following extension operation: choose a group consisting of characters c, and add some number of characters c to the group so that the size of the group is three or more.
For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get "helloo" since the group "oo" has a size less than three. Also, we could do another extension like "ll" -> "lllll" to get "helllllooo". If s = "helllllooo", then the query word "hello" would be stretchy because of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = s.
Return the number of query strings that are stretchy.


** Example 1: **
Input: s = "heeellooo", words = ["hello", "hi", "helo"]
Output: 1
Explanation:
We can extend "e" and "o" in the word "hello" to get "heeellooo".
We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.

** Example 2: **
Input: s = "zzzzzyyyyy", words = ["zzyy","zy","zyy"]
Output: 3


** Constraints: **
1 <= s.length, words.length <= 100
1 <= words[i].length <= 100
s and words[i] consist of lowercase letters.
"""

from utils.timer import timer
from collections import defaultdict


def get_short_word(s):
    short_word = ""
    tmp = ""
    for c in s:
        if c not in tmp:
            if len(tmp) > 2:
                short_word += tmp[0]
            else:
                short_word += tmp
            tmp = c
        elif c in tmp:
            tmp += c
    if len(tmp) > 2:
        short_word += tmp[0]
    else:
        short_word += tmp
    return short_word


def check_two_word(s1, s2):
    pointer_1 = pointer_2 = 0
    tmp_list = [False] * len(s1)
    while (pointer_1 < len(s1)) and (pointer_2 < len(s2)):
        if s1[pointer_1] == s2[pointer_2]:
            tmp_list[pointer_1] = True
            pointer_2 += 1
            pointer_1 += 1
        elif :
            pointer_2 += 1
    return all(tmp_list)

def check_word(c_i_list, s2):
    pointer_1 = pointer_2 = 0
    tmp_list = [False] * len(s1)
    while pointer_1 < len(s1) and pointer_2 < len(s2):
        if s1[pointer_1] == s2[pointer_2]:
            tmp_list[pointer_1] = True
            pointer_2 += 1
        else:
            pointer_1 += 1
    return all(tmp_list)

@timer
def solution(s: str, words: list) -> int:
    result = 0
    org_short_word = get_short_word(s)
    c_i_list = [(c, i) for c, i in enumerate(org_short_word)]
    for w in words:
        target_short_word = get_short_word(w)
        if check_two_word(org_short_word, target_short_word):
            result += 1
    return result



solution("heeellooo", ["hello", "hi", "helo"])      # Output: 1
solution("zzzzzyyyyy", ["zzyy","zy","zyy"])         # Output: 3