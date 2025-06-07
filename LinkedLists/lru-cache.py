# Date: 2025-05-28
# Author: Sparsha Srinath
# Leetcode (LRU Cache): https://leetcode.com/problems/lru-cache/
# Tags: Linked List, Hash Map, Design, LRU
# Time Complexity: O(1) for both get and put operations
# Space Complexity: O(capacity)

class Node:
    def __init__(self, key=None, value=None, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class List:
    def __init__(self):
        self.head = Node()  
        self.tail = Node()  
        self.head.next = self.tail
        self.tail.prev = self.head
        self.count = 0
    
    def insert(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node
        self.count += 1
    
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
        self.count -= 1

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.list = List()

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.list.remove(node)
            self.list.insert(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.list.remove(node)
            node.value = value
            self.list.insert(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self.list.insert(node)
            if self.list.count > self.capacity:
                lru = self.list.head.next
                self.list.remove(lru)
                del self.cache[lru.key]
