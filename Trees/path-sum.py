# LeetCode: https://leetcode.com/problems/path-sum/
# Problem: 112. Path Sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        Determines if the tree has a root-to-leaf path such that the sum of the node values 
        along the path equals the given target sum.

        Args:
            root (Optional[TreeNode]): The root node of the binary tree.
            targetSum (int): The desired path sum to be checked.

        Returns:
            bool: True if such a path exists, False otherwise.
        """

        def dfs(node, path_sum):
            if not node:
                return False

            # Add current node's value to the running sum
            path_sum += node.val

            # If it's a leaf node, check if the path sum matches targetSum
            if not node.left and not node.right:
                return path_sum == targetSum

            # Recurse left and right
            left = dfs(node.left, path_sum)
            right = dfs(node.right, path_sum)

            # Return True if either subtree has a valid path
            return left or right

        return dfs(root, 0)
