from utils.listnode import create_list_node, print_node, ListNode


def solution1(head, n):
    node_list = []
    node = head
    while node:
        node_list.append(node)
        node = node.next

    if len(node_list) == 1:
        head = None
    elif n == 1:
        node_list[-n - 1].next = None
    elif n == len(node_list):
        head = head.next
    else:
        node_list[-n - 1].next = node_list[-n + 1]
    return head


l1 = [1,2,3,4,5]
l1 = create_list_node(l1)
remove = 2
r = solution1(l1, remove)
print_node(r)
