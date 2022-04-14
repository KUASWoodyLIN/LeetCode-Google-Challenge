"""
  Decode String

Given an encoded string, return its decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc.
Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].


Example 1:
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:
Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"


Constraints:
1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
"""
from utils.timer import timer


class Solution:
    @timer
    def decodeString(self, s: str) -> str:
        stack = []
        switch = False
        num_tmp = ''
        for c in s:
            if c == ']':
                switch = True

            if switch:
                tmp = ''
                while switch:
                    pre_c = stack.pop()
                    if pre_c == '[':
                        plus = int(stack.pop())
                        switch = False
                        stack.append(tmp * int(plus))
                    else:
                        tmp = pre_c + tmp
            else:
                if 48 <= ord(c) <= 57:
                    num_tmp += c
                else:
                    if num_tmp:
                        stack.append(num_tmp)
                        num_tmp = ''
                    stack.append(c)
        return ''.join(stack)






S = Solution()
S.decodeString("3[a]2[bc]")         # Output: "aaabcbc"
S.decodeString("3[a2[c]]")          # Output: "accaccacc"
S.decodeString("2[abc]3[cd]ef")     # Output: "abcabccdcdcdef"
S.decodeString("100[leetcode]")
