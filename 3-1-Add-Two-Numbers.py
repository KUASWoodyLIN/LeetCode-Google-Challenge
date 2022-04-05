from utils.timer import timer
from utils.listnode import create_list_node, print_node, ListNode


@timer
def solution1(l1, l2):
    carry = 0
    node1 = l1
    node2 = l2
    while node1 and node2:
        tmp = node1.val + node2.val + carry
        carry = tmp // 10
        node1.val = tmp % 10
        prev = node1
        node1 = node1.next
        node2 = node2.next
    if node2 and not node1:
        prev.next = node2
        node1 = node2

    while carry == 1:
        if node1:
            tmp = carry + node1.val
            carry = tmp // 10
            node1.val = tmp % 10
            prev = node1
            node1 = node1.next
        else:
            prev.next = ListNode(carry)
            carry = 0
    return l1


def solution2(l1, l2):
    cur_node = dummy_head_node = ListNode(0)
    carry = 0
    node1 = l1
    node2 = l2
    while node1 or node2:
        v1 = node1.val if node1 else 0
        v2 = node2.val if node2 else 0
        tmp = v1 + v2 + carry
        carry = tmp // 10
        cur_node.next = ListNode(tmp % 10)
        cur_node = cur_node.next
        node1 = node1.next if node1 else None
        node2 = node2.next if node2 else None
    if carry:
        cur_node.next = ListNode(carry)
    return dummy_head_node.next


# l1 = [9,9,9,9,9,9,9]
# l2 = [9,9,9,9]
l1 = [2,4,9]
l2 = [5,6,4,9]
l1 = create_list_node(l1)
l2 = create_list_node(l2)
# r = solution1(l1, l2)
r = solution2(l1, l2)

print_node(r)
