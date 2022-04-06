"""
  Word Squares

Given an array of unique strings words, return all the word squares you can build from words. The same word from words can be used multiple times. You can return the answer in any order.
A sequence of strings forms a valid word square if the kth row and column read the same string, where 0 <= k < max(numRows, numColumns).
For example, the word sequence ["ball","area","lead","lady"] forms a word square because each word reads the same both horizontally and vertically.


Example 1:
Input: words = ["area","lead","wall","lady","ball"]
Output: [["ball","area","lead","lady"],["wall","area","lead","lady"]]
Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).

Example 2:
Input: words = ["abat","baba","atan","atal"]
Output: [["baba","abat","baba","atal"],["baba","abat","baba","atan"]]
Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).


Constraints:
1 <= words.length <= 1000
1 <= words[i].length <= 4
All words[i] have the same length.
words[i] consists of only lowercase English letters.
All words[i] are unique.
"""
from utils.timer import timer

class Solution:
    def __init__(self):
        self.save_words_temp = []
        self.result = []

    @timer
    def wordSquares(self, words: list) -> list:
        self.words_set = set(words)
        self.N = len(words[0])
        for w in words:
            save_words_temp = [w]
            self.backtracking(1, save_words_temp)
        return self.result

    def backtracking(self, step, save_words_temp):
        if self.N == step:
            self.result.append(save_words_temp.copy())
            return

        prefix = ''.join([w[step] for w in save_words_temp])
        for w in self.words_set:
            if w.startswith(prefix):
                save_words_temp.append(w)
                self.backtracking(step+1, save_words_temp)
                save_words_temp.pop()

s = Solution()
s.wordSquares(["area","lead","wall","lady","ball"])
# s.wordSquares(["abat","baba","atan","atal"])
# Output: [["baba","abat","baba","atal"],["baba","abat","baba","atan"]]
