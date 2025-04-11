# LeetCode: https://leetcode.com/problems/count-complete-tree-nodes/
# Problem: 222. Count Complete Tree Nodes

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        """
        Counts the number of nodes in a complete binary tree using BFS.

        Args:
            root (Optional[TreeNode]): The root of the binary tree.

        Returns:
            int: The total number of nodes in the tree.
        """
        if not root:
            return 0

        q = deque([root])
        num_nodes = 0

        while q:
            qLen = len(q)
            for _ in range(qLen):
                node = q.popleft()
                if node:
                    num_nodes += 1
                    q.append(node.left)
                    q.append(node.right)

        return num_nodes
