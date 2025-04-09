# LeetCode Problem: Vertical Order Traversal of a Binary Tree
# Link: https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

from collections import defaultdict, deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Performs vertical order traversal of a binary tree.

        Time Complexity: O(n log n), due to sorting nodes within each column.
        Space Complexity: O(n), for storing nodes in the map.
        """

        res = defaultdict(list)               # Dictionary to map column index to list of nodes
        q = deque([(root, 0, 0)])             # Queue for BFS: (node, row, column)

        while q:
            node, row, col = q.popleft()

            if node:
                # Append a tuple with row and value to help with sorting
                res[col].append((row, node.val))
                q.append((node.left, row + 1, col - 1))
                q.append((node.right, row + 1, col + 1))

        result = []

        # Sort columns from left to right
        for col in sorted(res.keys()):
            # Sort first by row, then by value
            column_nodes = sorted(res[col], key=lambda x: (x[0], x[1]))
            result.append([val for _, val in column_nodes])

        return result
