# LeetCode Problem: Maximum Depth of Binary Tree
# Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Returns the maximum depth (height) of the binary tree.
        The depth is the number of nodes along the longest path from the root down to the farthest leaf node.

        Time Complexity: O(n) - we visit each node once
        Space Complexity: O(h) - h is the height of the tree (due to the recursion stack)
