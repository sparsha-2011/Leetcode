# LeetCode Problem: Subtree of Another Tree
# Link: https://leetcode.com/problems/subtree-of-another-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Determines if `subRoot` is a subtree of `root`.
        A subtree of a binary tree is a tree that consists of a node in the tree and all of its descendants.

        Time Complexity: O(m * n), where m = number of nodes in `root`, and n = number of nodes in `subRoot`
        Space Complexity: O(h), where h = height of the tree (due to recursion stack)
        """

        # Base cases
        if subRoot is None:
            return True  # An empty tree is always a subtree
        if root is None:
            return False  # Non-empty tree can't be a subtree of an empty one

        # If the trees match at the current node, return True
        if self.sameTree(root, subRoot):
            return True

        # Otherwise, check recursively in the left and right subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Helper function that checks if two trees are exactly the same.

        Time Complexity: O(n), where n = number of nodes being compared
        """

        # If both nodes are None, they are the same
        if not root and not subRoot:
            return True

        # If both nodes exist and values match, check their left and right children
        if root and subRoot and root.val == subRoot.val:
            return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)

        # Otherwise, they are not the same
        return False
