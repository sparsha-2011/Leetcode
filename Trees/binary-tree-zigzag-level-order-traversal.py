# LeetCode Problem: Binary Tree Zigzag Level Order Traversal
# Link: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Returns the zigzag level order traversal of a binary tree.

        Time Complexity: O(n), where n is the number of nodes in the tree.
        Space Complexity: O(n), for the queue and result list.
        """

        if not root:
            return []

        q = deque([root])  # Queue for BFS
        level_num = 0      # Track the current level
        res = []           # Final result list

        while q:
            q_length = len(q)
            level = []

            for _ in range(q_length):
                node = q.popleft()

                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            if level:
                # Reverse level list if it's an odd-numbered level (zigzag)
                if level_num % 2 == 1:
                    level.reverse()

                res.append(level)
                level_num += 1

        return res
