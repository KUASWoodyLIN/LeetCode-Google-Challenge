from collections import defaultdict


class Solution:
    def findOrder(self, numCourses, prerequisites):
        adj_list = defaultdict(list)
        nodes_level = {i: 0 for i in range(numCourses)}
        for a, b in prerequisites:
            adj_list[b].append(a)
            nodes_level[a] += 1

        order_courses = []
        queue = [n for n, l in nodes_level.items() if l == 0]
        while queue:
            cur_node = queue.pop()
            order_courses.append(cur_node)
            if cur_node in adj_list:
                for next_node in adj_list[cur_node]:
                    nodes_level[next_node] -= 1
                    if nodes_level[next_node] == 0:
                        queue.append(next_node)
        if all([l==0 for l in nodes_level.values()]):
            return order_courses
        else:
            return []


S = Solution()
# r = S.findOrder(7, [['A', 'B'], ['C', 'B'], ['C', 'A'], ['E', 'A'], ['F', 'A'], ['E', 'F'], ['G', 'F'], ['F', 'D']])
r = S.findOrder(7, [[0, 1], [2, 1], [2, 0], [4, 0], [5, 0], [4, 5], [6, 5], [5, 3]])
# r = S.findOrder(2, [[0,1],[1,0]])
# r = S.findOrder(3, [[1, 0], [1, 2], [0, 1]])
print(r)
