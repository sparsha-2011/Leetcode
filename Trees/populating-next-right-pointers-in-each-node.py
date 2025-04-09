# LeetCode problem link: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """
        Populates each next pointer to point to its next right node in a perfect binary tree.
        If there is no next right node, the next pointer should be set to None.
        
        This solution uses level-order traversal (BFS) with a queue to connect the nodes at each level.
        
        Args:
        root (Node): The root node of the binary tree.
        
        Returns:
        Node: The root node with next pointers populated.
        """
        
        # If the tree is empty, return None
        if not root:
            return None
        
        # Initialize the queue for level-order traversal
        q = deque([root])
        
        # Perform a level-order traversal
        while q:
            # Get the number of nodes at the current level
            qLen = len(q)
            
            # Iterate over the nodes at the current level
            for i in range(qLen):
                # Pop a node from the queue
                node = q.popleft()
                
                # If this is not the last node at the level, set its next pointer to the next node in the queue
                if i < qLen - 1:
                    node.next = q[0]
                
                # Add the left and right children to the queue (if they exist)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        # Return the root as the problem asks for the tree with next pointers populated
        return root
