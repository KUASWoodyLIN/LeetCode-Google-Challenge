class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_tree_node(l: list):
    if not l:
        return []
    node_list = [TreeNode(i) for i in l]
    root = node_list[0]
    queue = [node_list.pop(0)]
    while queue:
        cur_node = queue.pop(0)
        if node_list:
            cur_node.left = node_list.pop(0)
            queue.append(cur_node.left)
        if node_list:
            cur_node.right = node_list.pop(0)
            queue.append(cur_node.right)
    return root


def print_tree(root):
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


if __name__ == '__main__':
    print_tree(create_tree_node([1, 2, 3, 4, 5, 6]))