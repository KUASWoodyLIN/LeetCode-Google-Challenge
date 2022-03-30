"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.



Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []


Constraints:
k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
"""
from utils.timer import timer
from queue import PriorityQueue


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_list_node(lists):
    list_node = []
    for i in range(len(lists)):
        tmp = ListNode(val=lists[i][-1])
        for j in range(len(lists[i])-2, -1, -1):
            tmp = ListNode(val=lists[i][j], next=tmp)
        list_node.append(tmp)
    return list_node


@timer
def solution1(lists: list) -> list:
    tmp = []
    for i in range(len(lists)):
        node = lists[i]
        while node is not None:
            tmp.append(node)
            node = node.next
    tmp = sorted(tmp, key=lambda x: x.val)
    for i in range(len(tmp)-1):
        tmp[i].next = tmp[i+1]
    return tmp[0] if tmp else None


@timer
def solution2(lists: list) -> list:
    head = point = ListNode(0)
    q = PriorityQueue()
    for l in lists:
        if l:
            q.put((l.val, l))
    while not q.empty():
        val, node = q.get()
        point.next = ListNode(val)
        point = point.next
        node = node.next
        if node:
            q.put((node.val, node))
    return head.next


list_node_lists = create_list_node([[1, 4, 5], [1, 3, 4], [2, 6]])
solution1(list_node_lists)
solution2(list_node_lists)