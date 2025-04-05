# LeetCode Problem: Diameter of Binary Tree
# Link: https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Returns the diameter of a binary tree. The diameter is the length of the longest path between any two nodes in the tree.
        This path may or may not pass through the root.

        Time Complexity: O(n) - we visit each node once
        Space Complexity: O(h) - h is the height of the tree (due to the recursion stack)
        """

        res = 0  # This will hold the result for the diameter
        
        # Helper function to calculate diameter
        def diameter(root: Optional[TreeNode]) -> int:
            nonlocal res
            if root is None:
                return 0  # If node is None, its height is 0

            # Recursively calculate the height of the left and right subtrees
            left = diameter(root.left)
            right = diameter(root.right)

            # Update the diameter if the sum of left and right height is larger
            res = max(res, left + right)

            # Return the height of the current node, which is max(left, right) + 1
            return 1 + max(left, right)

        # Start the recursion to calculate the diameter
        diameter(root)
        return res
