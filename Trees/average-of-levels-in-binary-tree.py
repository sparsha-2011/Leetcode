# LeetCode: https://leetcode.com/problems/average-of-levels-in-binary-tree/
# Problem: 637. Average of Levels in Binary Tree

from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        """
        Computes the average value of nodes on each level of the binary tree.

        Args:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            List[float]: A list of averages, one for each level of the tree.
        """
        if not root:
            return []

        result = []
        q = deque([root])

        while q:
            level_sum = 0
            level_len = len(q)

            for _ in range(level_len):
                node = q.popleft()
                level_sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            result.append(level_sum / level_len)

        return result
