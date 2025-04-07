# LeetCode Problem: Find Frequent Tree Sum
# Link: https://leetcode.com/problems/find-frequent-tree-sum/

from collections import defaultdict
from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        """
        Finds the most frequent subtree sums in a binary tree.

        Time Complexity: O(n), where n is the number of nodes in the tree.
        Space Complexity: O(n), where n is the number of unique subtree sums.

        :type root: TreeNode
        :rtype: List[int]
        """
        
        # Dictionary to store the frequency of each subtree sum
        frequency = defaultdict(int)

        def dfs(node):
            """
            Performs a depth-first search (DFS) to compute the sum of each subtree.

            :type node: TreeNode
            :rtype: int
            """
            if not node:
                return 0

            # Compute the sum of the left and right subtrees
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            # Calculate the sum for the current subtree
            subtree_sum = node.val + left_sum + right_sum

            # Update the frequency of the subtree sum
            frequency[subtree_sum] += 1

            return subtree_sum

        # Perform DFS to fill the frequency dictionary
        dfs(root)

        # Find the maximum frequency
        max_freq = max(frequency.values(), default=0)

        # Collect all subtree sums that have the maximum frequency
        most_freq = [s for s, freq in frequency.items() if max_freq == freq]

        return most_freq
