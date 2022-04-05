import math
import heapq
from utils.timer import timer


@timer
def solution1(points: list, k: int):
    tmp = []
    for i, p in enumerate(points):
        tmp.append((i, math.sqrt(p[0]*p[0]+p[1]*p[1])))
    tmp = sorted(tmp, key=lambda x: x[1])
    return [points[tmp[i][0]] for i in range(k)]


def distance(point: list):
    return point[0]*point[0]+point[1]*point[1]


@timer
def solution2(points: list, k: int):
    points.sort(key=distance)
    return points[:k]

@timer
def heapq_solution(points: list, k: int):
    heap = [(distance(p), i) for i, p in enumerate(points)]
    heapq.heapify(heap)
    return [points[heapq.heappop(heap)[1]] for i in range(k)]


solution1([[1,3],[-2,2]], 1)
solution2([[1,3],[-2,2]], 1)
heapq_solution([[1,3],[-2,2]], 1)