from collections import defaultdict


class Solution:
    def calcEquation(self, equations: list, values: list, queries: list) -> list:
        self.search_dict = defaultdict(dict)
        for (i, j), v in zip(equations, values):
            self.search_dict[i][j] = v
            self.search_dict[j][i] = v
            # search_dict[(i, j)] = v
            # search_dict[(j, i)] = 1 / v
        print(self.search_dict)

        self.ans_list = []
        for start, end in queries:
            ans = 1
            self.ans_flag = False
            for nxt, v in self.search_dict[start].items():
                ans *= v
                self.dfs(start, nxt, end, ans)

    def dfs(self, start, nxt, end, ans):
        if nxt == end:
            self.ans_flag = True
            self.ans_list.append(ans)

        else:
            for nxt, v in self.search_dict[nxt].items():
                ans *= v
                dfs


