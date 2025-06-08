# Author: Sparsha Srinath
# Date: 2025-06-08
# Url: https://leetcode.com/problems/merge-k-sorted-lists/
# Tags: Linked List, Heap, Priority Queue, Merge K Sorted Lists
# Description: Merge k sorted linked lists using a min-heap with a NodeWrapper class

from typing import List, Optional
import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node: ListNode):
        self.node = node

    def __lt__(self, other: "NodeWrapper") -> bool:
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        res = ListNode(0)
        cur = res
        minHeap = []

        for lst in lists:
            if lst is not None:
                heapq.heappush(minHeap, NodeWrapper(lst))

        while minHeap:
            node_wrapper = heapq.heappop(minHeap)
            cur.next = node_wrapper.node
            cur = cur.next
            
            if node_wrapper.node.next:
                heapq.heappush(minHeap, NodeWrapper(node_wrapper.node.next))
        
        return res.next


##Approach 2
from typing import List, Optional
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        
        # Initialize heap with the first node of each list and its index
        for i, lst in enumerate(lists):
            if lst:
                heapq.heappush(minHeap, (lst.val, i, lst))
        
        dummy = ListNode(0)
        current = dummy
        
        while minHeap:
            val, i, node = heapq.heappop(minHeap)
            current.next = node
            current = current.next
            
            if node.next:
                heapq.heappush(minHeap, (node.next.val, i, node.next))
        
        return dummy.next
