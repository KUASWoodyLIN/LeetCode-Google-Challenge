from utils.timer import timer


class Solution:
    def __init__(self):
        self.queue = []
        self.queue_tmp = []
        self.x_max = 0
        self.y_max = 0

    def longestIncreasingPath(self, matrix) -> int:
        self.y_max, self.x_max = len(matrix), len(matrix[0])
        longest_path = 0
        for y in range(self.y_max):
            for x in range(self.x_max):
                cur_max = 0
                self.queue.append((y, x))

                while self.queue:
                    node = self.queue.pop(0)
                    self.dfs(node, matrix)
                    if not self.queue and self.queue_tmp:
                        cur_max += 1
                        self.queue = self.queue_tmp.copy()
                        self.queue_tmp.clear()
                longest_path = max(longest_path, cur_max)
        return longest_path + 1

    def dfs(self, node, matrix):
        y, x = node
        new_y = y - 1
        if (new_y >= 0) and (matrix[y][x] < matrix[new_y][x]):
            self.queue_tmp.append((new_y, x))
        new_y = y + 1
        if (new_y < self.y_max) and (matrix[y][x] < matrix[new_y][x]):
            self.queue_tmp.append((new_y, x))
        new_x = x - 1
        if (new_x >= 0) and (matrix[y][x] < matrix[y][new_x]):
            self.queue_tmp.append((y, new_x))
        new_x = x + 1
        if (new_x < self.x_max) and (matrix[y][x] < matrix[y][new_x]):
            self.queue_tmp.append((y, new_x))


class SolutionV2:
    def longestIncreasingPath(self, matrix) -> int:
        longest_path = 0
        self.y_max, self.x_max = len(matrix), len(matrix[0])
        search_map = [[[] for x in range(len(matrix[0]))] for y in range(len(matrix))]
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                search_map[y][x].extend(self.next_steps(matrix, y, x))

        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                self.cur_max = {}
                seen = {}
                level = self.bdf(search_map, (y, x), 0, seen)
                longest_path = max(longest_path, level)
        return longest_path

    def bdf(self, search_map, node, level, seen):
        key = '{},{}'.format(node[0], node[1])
        if key in seen:
            max_tmp = max(level + seen[key], seen[key])
            seen[key] = max_tmp - level
            return max_tmp
        level += 1
        tmp = []
        nodes = search_map[node[0]][node[1]]
        for n in nodes:
            tmp.append(self.bdf(search_map, n, level, seen))
        if nodes:
            max_tmp = max(tmp)
            seen[key] = max_tmp - level + 1
            return max_tmp
        else:
            seen[key] = 1
            return level

    def next_steps(self, matrix, y, x) -> list:
        tmp = []
        new_y = y - 1
        if (new_y >= 0) and (matrix[y][x] < matrix[new_y][x]):
            tmp.append((new_y, x))
        new_y = y + 1
        if (new_y < self.y_max) and (matrix[y][x] < matrix[new_y][x]):
            tmp.append((new_y, x))
        new_x = x - 1
        if (new_x >= 0) and (matrix[y][x] < matrix[y][new_x]):
            tmp.append((y, new_x))
        new_x = x + 1
        if (new_x < self.x_max) and (matrix[y][x] < matrix[y][new_x]):
            tmp.append((y, new_x))
        return tmp


class SolutionV3:
    def __init__(self):
        self.y_max = 0
        self.x_max =0
        self.caches = []

    def longestIncreasingPath(self, matrix) -> int:
        self.y_max = len(matrix)
        self.x_max = len(matrix[0])
        self.caches = [[0 for _ in range(self.x_max)] for _ in range(self.y_max)]

        ans = 0
        for y in range(self.y_max):
            for x in range(self.x_max):
                ans = max(ans, self.dfs(matrix, y, x))
        return ans

    def dfs(self, matrix, y, x):
        new_y = y - 1
        if self.caches[y][x]:
            return self.caches[y][x]
        if (new_y >= 0) and (matrix[y][x] < matrix[new_y][x]):
            self.caches[y][x] = max(self.caches[y][x], self.dfs(matrix, new_y, x))
        new_y = y + 1
        if (new_y < self.y_max) and (matrix[y][x] < matrix[new_y][x]):
            self.caches[y][x] = max(self.caches[y][x], self.dfs(matrix, new_y, x))
        new_x = x - 1
        if (new_x >= 0) and (matrix[y][x] < matrix[y][new_x]):
            self.caches[y][x] = max(self.caches[y][x], self.dfs(matrix, y, new_x))
        new_x = x + 1
        if (new_x < self.x_max) and (matrix[y][x] < matrix[y][new_x]):
            self.caches[y][x] = max(self.caches[y][x], self.dfs(matrix, y, new_x))
        self.caches[y][x] += 1
        return self.caches[y][x]


# S = Solution()
# S = SolutionV2()
S = SolutionV3()
# test = [[7,7,5],[2,4,6],[8,2,0]]                        # Output: 4
# test = [[9,9,4],[6,6,8],[2,1,1]]                        # Output: 4
# test = [[1, 2, 3], [6, 5, 4], [7, 8, 9]]                # Output: 9
test = [[1, 2, 3], [6, 5, 4], [7, 8, 9], [0, 0, 0]]     # Output: 9
# test = [[1, 2, 3, 4], [8, 7, 6, 5], [9, 10, 11, 12], [0, 0, 0, 0]]    # Output: 12
# test = [[0,1,2,3,4,5,6,7,8,9],[19,18,17,16,15,14,13,12,11,10],[20,21,22,23,24,25,26,27,28,29],[39,38,37,36,35,34,33,32,31,30],[40,41,42,43,44,45,46,47,48,49],[59,58,57,56,55,54,53,52,51,50],[60,61,62,63,64,65,66,67,68,69],[79,78,77,76,75,74,73,72,71,70],[80,81,82,83,84,85,86,87,88,89],[99,98,97,96,95,94,93,92,91,90],[100,101,102,103,104,105,106,107,108,109],[119,118,117,116,115,114,113,112,111,110],[120,121,122,123,124,125,126,127,128,129],[139,138,137,136,135,134,133,132,131,130],[0,0,0,0,0,0,0,0,0,0]]
# test = [[5,14,7,6,10,4,8,9,5,1,11,15],[9,12,9,11,6,7,2,4,2,10,15,0],[11,6,2,5,9,16,15,4,0,17,18,8],[3,7,5,16,12,18,4,0,12,12,8,18],[3,18,18,17,1,13,11,15,4,14,13,17],[14,11,13,7,4,10,5,5,5,11,10,5],[16,1,10,15,17,10,11,14,6,2,8,4],[15,11,6,12,5,7,7,8,11,17,19,12],[16,17,7,15,8,11,7,9,18,8,9,16],[7,13,4,9,4,5,0,6,4,2,10,13],[9,16,12,10,1,10,16,2,16,10,9,18],[12,7,16,0,2,17,13,9,8,2,14,15],[1,9,13,2,4,0,13,14,9,2,16,15],[6,7,12,14,10,0,11,12,4,8,2,18],[3,6,13,15,7,16,9,14,12,0,8,11]]
print(S.longestIncreasingPath(test))
