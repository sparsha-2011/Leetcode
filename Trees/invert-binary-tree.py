# LeetCode Problem: Invert Binary Tree
# Link: https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        This function takes the root of a binary tree and inverts it.
        That is, it swaps every left and right subtree recursively.

        Time Complexity: O(n), where n is the number of nodes in the tree
        Space Complexity: O(h), where h is the height of the tree (due to recursion stack)
        """
        
        # Base case: if the tree is empty
        if not root:
            return None

        # Swap the left and right children
        root.left, root.right = root.right, root.left

        # Recursively invert the left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        # Return the root of the inverted tree
        return root
