class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_list_node(l: list):
    n = first_node = ListNode(l[0])
    for i in range(1, len(l)):
        n.next = ListNode(l[i])
        n = n.next
    return first_node


def print_node(node):
    tmp = []
    while node:
        tmp.append(node.val)
        node = node.next
    print(tmp)



