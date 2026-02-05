# Author: Sparsha Srinath
# Date: 2025-08-13
# Problem: Implement Trie (Prefix Tree)
# Link: https://leetcode.com/problems/implement-trie-prefix-tree/
# Tags: Trie, String, Data Structure
# Time Complexity:
#   insert   -> O(L)
#   search   -> O(L)
#   startsWith -> O(L)
#   where L = length of the word
# Space Complexity: O(total characters stored in trie)

class Node:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
