from utils.timer import timer
from functools import cache


class SolutionV1:
    @timer
    def numberOfPatterns(self, m: int, n: int) -> int:
        self.cross_pattern_dict = {
            (1, 3): 2, (3, 1): 2,
            (4, 6): 5, (6, 4): 5,
            (7, 9): 8, (9, 7): 8,
            (1, 7): 4, (7, 1): 4,
            (2, 8): 5, (8, 2): 5,
            (3, 9): 6, (9, 3): 6,
            (1, 9): 5, (9, 1): 5,
            (3, 7): 5, (7, 3): 5,
        }
        self.result = 0
        self.m, self.n = m, n
        for i in range(1, 10):
            keys = [i]
            self.backtracking(keys)

        return self.result

    def backtracking(self, keys):
        tmp_bool = (len(keys) >= self.m and len(keys) <= self.n)
        if tmp_bool:
            self.result += 1

        if tmp_bool or (len(keys) < self.m):
            for next_p in range(1, 10):
                cross_pattern = self.cross_pattern_dict.get((keys[-1], next_p), True)
                if (next_p not in keys) and ((cross_pattern is True) or (cross_pattern in keys)):
                    keys.append(next_p)
                    self.backtracking(keys)
                    keys.pop()


class SolutionV2:
    @timer
    def numberOfPatterns(self, m: int, n: int) -> int:
        self.cross_pattern_dict = {
            (1, 3): 2, (3, 1): 2,
            (4, 6): 5, (6, 4): 5,
            (7, 9): 8, (9, 7): 8,
            (1, 7): 4, (7, 1): 4,
            (2, 8): 5, (8, 2): 5,
            (3, 9): 6, (9, 3): 6,
            (1, 9): 5, (9, 1): 5,
            (3, 7): 5, (7, 3): 5,
        }
        self.pattern_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        self.result = 0
        self.m, self.n = m, n
        for i in range(1, 10):
            keys = {i}
            self.backtracking(keys, i)
        return self.result

    def backtracking(self, keys, pre_p):
        if tmp_bool := (self.m <= len(keys) <= self.n):
            self.result += 1
        if tmp_bool or (len(keys) < self.m):
            for next_p in self.pattern_set - keys:
                cross_pattern = self.cross_pattern_dict.get((pre_p, next_p), True)
                if (next_p not in keys) and ((cross_pattern is True) or (cross_pattern in keys)):
                    keys.add(next_p)
                    self.backtracking(keys, next_p)
                    keys.remove(next_p)


class SolutionV3:
    @timer
    def numberOfPatterns(self, m: int, n: int) -> int:
        self.cross_pattern_dict = {
            (1, 3): 2, (3, 1): 2,
            (4, 6): 5, (6, 4): 5,
            (7, 9): 8, (9, 7): 8,
            (1, 7): 4, (7, 1): 4,
            (2, 8): 5, (8, 2): 5,
            (3, 9): 6, (9, 3): 6,
            (1, 9): 5, (9, 1): 5,
            (3, 7): 5, (7, 3): 5,
        }
        self.pattern_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        self.result = 0
        self.m, self.n = m, n
        for i in range(1, 10):
            keys = {i}
            self.backtracking(keys, i)
        return self.result

    def backtracking(self, keys, pre_p):
        if len(keys) == self.n:
            self.result += 1
            return

        if len(keys) >= self.m:
            self.result += 1

        for next_p in self.pattern_set - keys:
            cross_pattern = self.cross_pattern_dict.get((pre_p, next_p), True)
            if (next_p not in keys) and ((cross_pattern is True) or (cross_pattern in keys)):
                keys.add(next_p)
                self.backtracking(keys, next_p)
                keys.remove(next_p)


class SolutionV4:
    @timer
    def numberOfPatterns(self, m: int, n: int) -> int:
        self.cross_pattern_dict = {
            (1, 3): 2, (3, 1): 2,
            (4, 6): 5, (6, 4): 5,
            (7, 9): 8, (9, 7): 8,
            (1, 7): 4, (7, 1): 4,
            (2, 8): 5, (8, 2): 5,
            (3, 9): 6, (9, 3): 6,
            (1, 9): 5, (9, 1): 5,
            (3, 7): 5, (7, 3): 5,
        }
        self.pattern_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        self.m, self.n = m, n
        total_combos = 0
        for num in range(1, 10):
            combos = self.backtracking(1 << num, num)
            total_combos += combos
        return total_combos

    @cache
    def backtracking(self, visited, pre_p):
        visited_count = visited.bit_count()

        if visited_count == self.n:
            return 1

        combos = 0
        if visited_count >= self.m:
            combos = 1

        for next_p in range(1, 10):
            if self.is_visited(visited, next_p):
                continue

            cross_pattern = self.cross_pattern_dict.get((pre_p, next_p))
            if not cross_pattern or self.is_visited(visited, cross_pattern):
                num_mask = 1 << next_p
                next_visited = visited | num_mask
                combos += self.backtracking(next_visited, next_p)
        return combos

    def is_visited(self, visited, num):
        mask = 1 << num
        return visited == visited | mask


s1 = SolutionV1()
s2 = SolutionV2()
s3 = SolutionV3()
s4 = SolutionV4()
s1.numberOfPatterns(1, 8)
s2.numberOfPatterns(1, 8)
s3.numberOfPatterns(1, 8)
s4.numberOfPatterns(1, 8)
