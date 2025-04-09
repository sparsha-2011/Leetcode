# LeetCode Problem: 993. Cousins in Binary Tree
# Link: https://leetcode.com/problems/cousins-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        """
        Determines whether two nodes with values x and y are cousins.
        Two nodes are cousins if they are on the same level and have different parents.

        Time Complexity: O(n) - where n is the number of nodes in the tree
        Space Complexity: O(h) - where h is the height of the tree (due to recursion stack)
        """

        self.x_parent = self.y_parent = None
        self.x_depth = self.y_depth = -1

        def dfs(node, parent, depth):
            if not node:
                return

            if node.val == x:
                self.x_parent = parent
                self.x_depth = depth
            elif node.val == y:
                self.y_parent = parent
                self.y_depth = depth

            dfs(node.left, node, depth + 1)
            dfs(node.right, node, depth + 1)

        dfs(root, None, 0)

        return (
            self.x_depth == self.y_depth and 
            self.x_parent != self.y_parent
        )
