# Author: Sparsha Srinath
# Date: 2026-01-06
# Problem: Binary Tree Maximum Path Sum
# Link: https://leetcode.com/problems/binary-tree-maximum-path-sum/
# Tags: Binary Tree, DFS, Recursion, Dynamic Programming
# Time Complexity: O(n), where n is the number of nodes in the tree
# Space Complexity: O(h), where h is the height of the tree (recursion stack)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Initialize the global maximum path sum with root value
        max_sum = root.val

        def maxSum(root):
            nonlocal max_sum  # Allows updating max_sum from the outer scope

            # Base case: empty node contributes 0 to path sum
            if not root:
                return 0

            # Recursively compute maximum path sums from left and right subtrees
            maxLeft = maxSum(root.left)
            maxRight = maxSum(root.right)

            # Ignore negative path sums (better to not include them)
            maxLeft = max(maxLeft, 0)
            maxRight = max(maxRight, 0)

            # Update global maximum considering the path passing through current node
            max_sum = max(max_sum, root.val + maxLeft + maxRight)

            # Return maximum gain if extending path to parent
            return root.val + max(maxLeft, maxRight)

        # Start DFS traversal from root
        maxSum(root)

        # Return the maximum path sum found
        return max_sum
