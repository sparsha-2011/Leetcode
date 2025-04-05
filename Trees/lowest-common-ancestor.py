# LeetCode Problem: Lowest Common Ancestor of a Binary Search Tree
# Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Finds the lowest common ancestor (LCA) of two nodes in a Binary Search Tree (BST).

        In a BST, for any node:
        - The left subtree has nodes with values less than the node’s value.
        - The right subtree has nodes with values greater than the node’s value.

        Time Complexity: O(log n) on average for a balanced BST, O(n) in the worst case (unbalanced)
        Space Complexity: O(1)
        """

        cur = root

        while cur:
            # If both p and q are greater than current node, move to the right subtree
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            # If both p and q are smaller than current node, move to the left subtree
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                # We've found the split point where p and q diverge — this is the LCA
                return cur
