# LeetCode Problem: Binary Tree Right Side View
# Link: https://leetcode.com/problems/binary-tree-right-side-view/

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Returns the values of the nodes visible from the right side of the binary tree.

        This implementation uses Breadth-First Search (BFS) and captures
        the last node (rightmost) at each level.

        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(n) for queue and result list
        """

        res = []
        q = deque([root])

        while q:
            rightNode = None
            qLen = len(q)

            for _ in range(qLen):
                node = q.popleft()
                if node:
                    rightNode = node  # The last node processed at this level is the rightmost
                    q.append(node.left)
                    q.append(node.right)
            
            if rightNode:
                res.append(rightNode.val)

        return res

        # Optional DFS version (commented out):
        # def dfs(node, level):
        #     if not node:
        #         return
        #     if level == len(res):
        #         res.append(node.val)
        #     dfs(node.right, level + 1)
        #     dfs(node.left, level + 1)
        #
        # dfs(root, 0)
        # return res
