# LeetCode Problem: Same Tree
# Link: https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Checks if two binary trees are the same.
        Two binary trees are considered the same if they are structurally identical,
        and the nodes have the same value.

        Time Complexity: O(n), where n is the number of nodes in the tree
        Space Complexity: O(h), where h is the height of the tree (due to recursion stack)
        """
        
        # If both trees are None, they are the same (base case)
        if not p and not q:
            return True
        
        # If both trees are not None, check if their values match
        if p and q and p.val == q.val:
            # Recursively check left and right subtrees
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        # If one of the trees is None or the values don't match, return False
        return False
