from utils.treenode import create_tree_node, print_tree


from utils.timer import timer


@timer
def brute_force(root):
    if not root:
        return 0
    queue = [root]

    count = 1
    while queue:
        node = queue.pop(0)
        if node.left:
            queue.append(node.left)
            count += 1
        if node.right:
            queue.append(node.right)
            count += 1
    return count


@timer
def dfs_and_bfs(root):
    if not root:
        return 0
    level = 0
    cur_node = root.left
    while cur_node:
        level += 1
        cur_node = cur_node.left
    queue = [root]
    for i in range(level):
        tmp = []
        for n in queue:
            tmp.append(n.left)
            tmp.append(n.right)
        queue = tmp
    add = sum([True for n in queue if n])
    return 2**level + add -1


tree = create_tree_node([1,2,3,4,5,6])
# tree = create_tree_node([])
# tree = create_tree_node([2])
brute_force(tree)
dfs_and_bfs(tree)
print_tree(tree)
