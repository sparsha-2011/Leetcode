# Leetcode Problem: Flatten a Multilevel Doubly Linked List
# Link: https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
# Author: Sparsha Srinath
# Date: 2025-06-08
# Tags: Doubly Linked List, Recursion, DFS
# Time Complexity: O(n), where n is the total number of nodes
# Space Complexity: O(n) in the worst case due to recursion stack

class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        def dfs(node):
            curr = node
            last = None

            while curr:
                next_node = curr.next
                # If current node has a child, process the child list
                if curr.child:
                    child_head = curr.child
                    # Recursively flatten the child
                    child_tail = dfs(child_head)

                    # Splice the child into the main list
                    curr.next = child_head
                    child_head.prev = curr
                    curr.child = None

                    if next_node:
                        child_tail.next = next_node
                        next_node.prev = child_tail
                    last = child_tail
                    curr = next_node
                else:
                    last = curr
                    curr = curr.next
            return last

        dfs(head)
        return head
