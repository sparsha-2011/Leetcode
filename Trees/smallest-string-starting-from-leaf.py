# LeetCode: https://leetcode.com/problems/smallest-string-starting-from-leaf/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        # Initialize the smallest string to a lexicographically large string ('{' is just larger than 'z')
        smallest = '{'  
        
        # Helper function for Depth First Search (DFS)
        def dfs(node, path):
            nonlocal smallest
            if not node:
                return  # If the node is None, return immediately
            
            # Convert the current node's value to a character (using 'a' as base) and append it to the path
            path.append(chr(node.val + ord('a')))
            
            # If we reach a leaf node (node has no left or right child)
            if not node.left and not node.right:
                # Convert the path list to a string by reversing it (because we're building it from leaf to root)
                current_str = ''.join(path[::-1])
                
                # Compare with the smallest string and keep the lexicographically smallest one
                smallest = min(smallest, current_str)
            
            # Recursively search both left and right subtrees
            dfs(node.left, path)
            dfs(node.right, path)
            
            # Backtrack: Remove the last character added to the path (since we're done exploring that node)
            path.pop()
        
        # Start the DFS traversal from the root, with an empty path
        dfs(root, [])
        
        # Return the lexicographically smallest string found
        return smallest
