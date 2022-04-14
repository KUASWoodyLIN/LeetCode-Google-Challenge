"""
Example 1:
Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation:
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]

Example 2:
Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]

Example 3:
Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]
"""
from utils.timer import timer
from collections import defaultdict


class Solution:
    @timer
    def calcEquation(self, equations: list, values: list, queries: list) -> list:
        self.search_dict = defaultdict(dict)
        for (i, j), v in zip(equations, values):
            self.search_dict[i][j] = v
            self.search_dict[j][i] = 1 / v

        self.result_list = []
        for start, end in queries:
            plus_path = [start]
            self.ans_flag = False
            for nxt, v in self.search_dict[start].items():
                if self.ans_flag:
                    continue
                ans_list = [v]
                self.backtracking(nxt, end, ans_list, plus_path)

            if not self.ans_flag:
                self.result_list.append(-1)
        return self.result_list

    def backtracking(self, cur, end, ans_tmp, plus_path):
        if cur == end:
            ans = 1
            for v in ans_tmp:
                ans *= v
            self.result_list.append(ans)
            self.ans_flag = True
        elif cur not in plus_path:
            plus_path.append(cur)
            for nxt, v in self.search_dict[cur].items():
                if self.ans_flag:
                    continue
                ans_tmp.append(v)
                self.backtracking(nxt, end, ans_tmp, plus_path)
                ans_tmp.pop()
            plus_path.pop()


# equations = [["a","e"],["b","e"]]
# values = [4.0,3.0]
# queries = [["a","b"],["e","e"],["x","x"]]

# equations = [["a","b"],["b","c"]]
# values = [2.0,3.0]
# queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]

# equations = [["a","b"],["b","c"],["bc","cd"]]
# values = [1.5,2.5,5.0]
# queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
# Output: [3.75000,0.40000,5.00000,0.20000]

# equations = [["a","e"],["b","e"]]
# values = [4.0,3.0]
# queries = [["a","b"],["e","e"],["x","x"]]
# Output: [1.33333,1.00000,-1.00000]

# equations = [["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]]
# values = [3.0,4.0,5.0,6.0]
# queries = [["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]
# Output: [360.00000,0.00833,20.00000,1.00000,-1.00000,-1.00000]

equations = [["a","b"],["b","c"],["a","c"]]
values = [2.0,3.0,6.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
S = Solution()
S.calcEquation(equations, values, queries)

