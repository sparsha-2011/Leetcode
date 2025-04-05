# LeetCode Problem: Balanced Binary Tree
# Link: https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Returns True if the binary tree is balanced, and False otherwise.
        A balanced tree is defined as a tree where the depth of the two subtrees of every node never differ by more than 1.

        Time Complexity: O(n) - we visit each node once
        Space Complexity: O(h) - h is the height of the tree (due to recursion stack)
        """

        def dfs(root: Optional[TreeNode]) -> bool:
            """
            Helper function to perform Depth-First Search (DFS) to check if the tree is balanced and calculate its height.
            
            Returns a list where:
            - The first element is True if the subtree is balanced, otherwise False.
            - The second element is the height of the subtree.
            """
            if root is None:
                return [True, 0]  # Base case: an empty subtree is balanced with height 0

            # Recursively check the left and right subtrees
            left = dfs(root.left)
            right = dfs(root.right)

            # A tree is balanced if both left and right subtrees are balanced,
            # and the difference in heights is not more than 1
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            # Return whether the tree is balanced and its height
            return [balanced, 1 + max(left[1], right[1])]

        # The final result will be the balance status of the whole tree
        return dfs(root)[0]
