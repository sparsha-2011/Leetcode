# LeetCode Problem: Binary Tree Level Order Traversal
# Link: https://leetcode.com/problems/binary-tree-level-order-traversal/

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Performs a level order traversal (BFS) of a binary tree and returns a list of levels,
        where each level is a list of node values.

        Time Complexity: O(n), where n = number of nodes in the tree
        Space Complexity: O(n), for the queue and result storage
        """

        res = []  # Final result list of levels
        q = deque()  # Queue for BFS traversal
        q.append(root)

        while q:
            level = []
            qLen = len(q)

            for _ in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            if level:
                res.append(level)

        return res
