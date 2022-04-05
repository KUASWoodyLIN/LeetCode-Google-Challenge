from utils.timer import timer
from test_value.test_value import grid


def search_neighbors(node):
    y, x = node
    return [(y, x - 1), (y, x + 1), (y - 1, x), (y + 1, x)]


@timer
def solution1(grid: list) -> int:
    result = 0
    seen = set([(y, x) for y, outer in enumerate(grid) for x, inner in enumerate(outer) if inner == '1'])

    if len(seen) == 0:
        return result
    stack = [seen.pop()]
    while stack:
        node = stack.pop()
        neighbors = search_neighbors(node)
        for neighbor in neighbors:
            if neighbor in seen:
                seen.remove(neighbor)
                stack.append(neighbor)
        if len(stack) == 0:
            result += 1
            if len(seen) > 0:
                stack.append(seen.pop())
    return result


def bfs(grid, y, x):
    if y >= len(grid) or x >= len(grid[0]) or y < 0 or x < 0:
        return
    if grid[y][x] == '0':
        return
    else:
        grid[y][x] = '0'
    bfs(grid, y+1, x)
    bfs(grid, y-1, x)
    bfs(grid, y, x+1)
    bfs(grid, y, x-1)


@timer
def solution_bfs(grid: list) -> int:
    result = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '1':
                result += 1
                bfs(grid, y, x)
    return result



solution1(grid)
solution_bfs(grid)
# solution_bfs([["1","0","1","1","0","1","1"]])
# 1011011