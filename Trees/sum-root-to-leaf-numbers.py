# LeetCode Problem: Sum Root to Leaf Numbers
# Link: https://leetcode.com/problems/sum-root-to-leaf-numbers/

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """
        Calculates the sum of all numbers formed by root-to-leaf paths in the binary tree.

        Time Complexity: O(n), where n is the number of nodes in the tree.
        Space Complexity: O(h), where h is the height of the tree due to recursion stack.

        :type root: TreeNode
        :rtype: int
        """

        # DFS function to calculate the sum of root-to-leaf numbers
        def dfs(node, path):
            if not node:
                return 0

            # Append the current node's value to the path
            path += str(node.val)

            # If it's a leaf node, convert the path to an integer and return the value
            if not node.left and not node.right:
                return int(path)

            # Recurse on the left and right subtrees and accumulate the sums
            leftSum = dfs(node.left, path)
            rightSum = dfs(node.right, path)

            return leftSum + rightSum

        # Start the DFS from the root and return the sum of all root-to-leaf numbers
        return dfs(root, "")
