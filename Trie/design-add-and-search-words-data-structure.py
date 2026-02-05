# Author: Sparsha Srinath
# Date: 2025-08-13
# Problem: Design Add and Search Words Data Structure
# Link: https://leetcode.com/problems/design-add-and-search-words-data-structure/
# Tags: Trie, DFS, Backtracking, String
# Time Complexity:
#   addWord  -> O(L)
#   search   -> O(L) average, O(26^L) worst-case with wildcards
# Space Complexity: O(total characters stored in trie)

class Node:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.endOfWord = True 

    def search(self, word: str) -> bool:

        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]

            return cur.endOfWord

        return dfs(0, self.root)
