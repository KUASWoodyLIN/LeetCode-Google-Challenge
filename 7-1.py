from utils.timer import timer


class Solution:
    @timer
    def longestPalindrome(self, s: str) -> str:
        long = len(s)
        for i in range(long, 0, -1):
            for j in range(long - i + 1):
                if s[j:j + i] == s[j:j + i][::-1]:
                    return s[j:j + i]


class SolutionV2:
    def longestPalindrome(self, s: str) -> str:
        if s is "":
            return ""

        rev = s[::-1]
        dp = [[0 for i in range(len(s))] for j in range(len(s))]
        max_len = 0
        max_end = 0
        for i in range(len(s)):
            for j in range(len(s)):
                if s[i] == rev[j]:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_len:
                    if i - dp[i][j] + 1 == len(s) - 1 - j:
                        max_len = dp[i][j]
                        max_end = i

        return s[max_end - max_len + 1: max_end + 1]


input1 = "babad"
# Output: "bab"
S = Solution()
S = SolutionV2()
S.longestPalindrome(input1)