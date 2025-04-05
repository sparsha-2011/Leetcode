# LeetCode Problem: Validate Binary Search Tree
# Link: https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Determines if a binary tree is a valid binary search tree (BST).

        A binary search tree is valid if:
        - The left subtree of a node contains only nodes with values less than the node's value.
        - The right subtree of a node contains only nodes with values greater than the node's value.
        - Both the left and right subtrees must also be valid BSTs.

        This solution uses Depth-First Search (DFS) to recursively check each node's value
        against the allowed range, which changes as we move down the tree.

        Time Complexity: O(n), where n is the number of nodes in the tree.
        Space Complexity: O(h), where h is the height of the tree, due to the recursion stack.
        """

        def dfs(node, lower=float('-inf'), upper=float('inf')):
            """
            Helper function to perform DFS and check the validity of the BST.

            Args:
                node (TreeNode): The current node to check.
                lower (float): The lower bound for the current node's value.
                upper (float): The upper bound for the current node's value.

            Returns:
                bool: True if the subtree rooted at the current node is a valid BST, False otherwise.
            """
            if not node:
                return True

            val = node.val

            # Check if the current node's value is within the valid range
            if val <= lower or val >= upper:
                return False

            # Recursively check the left and right subtrees with updated bounds
            return dfs(node.left, lower, val) and dfs(node.right, val, upper)

        # Start the DFS with the root and the initial bounds (-inf, inf)
        return dfs(root)
