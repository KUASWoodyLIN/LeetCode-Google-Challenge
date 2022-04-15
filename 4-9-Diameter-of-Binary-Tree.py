"""
Diameter of Binary Tree

Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.

Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
Input: root = [1,2]
Output: 1


Constraints:
The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100
"""
from utils.treenode import create_tree_node
from utils.timer import timer


class Solution:
    @timer
    def diameterOfBinaryTree(self, root) -> int:
        self.tree_left_right_max = []
        r1, r2 = 0, 0
        if root.left:
            r2 = self.dfs(root.left, 1)
        if root.right:
            r1 = self.dfs(root.right, 1)
        self.tree_left_right_max.append(r1+r2)
        return max(self.tree_left_right_max)

    def dfs(self, node, count):
        r1, r2 = 0, 0
        if node.left:
            r1 = self.dfs(node.left, count+1)
        if node.right:
            r2 = self.dfs(node.right, count+1)
        self.tree_left_right_max.append(r1+r2-count-count)
        return max([count, r1, r2])


class SolutionV2:
    def diameterOfBinaryTree(self, root) -> int:
        self. diameter = 0
        self.longest_path(root)
        return self.diameter

    def longest_path(self, node):
        if not node:
            return 0
        # recursively find the longest path in
        # both left child and right child
        left_path = self.longest_path(node.left)
        right_path = self.longest_path(node.right)

        # update the diameter if left_path plus right_path is larger
        self.diameter = max(self.diameter, left_path + right_path)

        # return the longest one between left_path and right_path;
        # remember to add 1 for the path connecting the node and its parent
        return max(left_path, right_path) + 1


tree_root = create_tree_node([1,2,3,4,5])
# tree_root = create_tree_node([1,2])
# tree_root = create_tree_node([1,2,3])
# tree_root = create_tree_node([3,1,None,None,2])
# tree_root = create_tree_node([3,1,None,2,None,None,4])
# tree_root = create_tree_node([4,2,None,3,1,None,None,5])

S = Solution()
S.diameterOfBinaryTree(tree_root)
# [3,1,null,null,2]
# TreeNode{val: 1, left: TreeNode{val: 2, left: TreeNode{val: 4, left: None, right: None}, \
#                                         right: TreeNode{val: 5, left: None, right: None}}
#                , right: TreeNode{val: 3, left: None,
#                                          right: None}}
