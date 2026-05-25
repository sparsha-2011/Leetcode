# Author: Sparsha Srinath
# URL: https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/
# Date: 2026-05-24
# Tags: arrays, hash-map, design, randomized
# Description:
#   Implements a collection that supports insert, remove, and getRandom in O(1)
#   average time, allowing duplicate values. Uses a list for O(1) random access
#   and a hashmap (value → list of indices) for O(1) lookup. Remove works by
#   swapping the target with the last element and popping — avoids O(n) shift.
#   Skip swap if target is already the last element. When swapping, update the
#   swapped element's index list: remove old index, add new index.
#
# Input: insert(val), remove(val), getRandom()
# Output: bool for insert/remove, int for getRandom
#
# Example:
#   insert(1) → True
#   insert(1) → False (duplicate, but still added)
#   insert(2) → True
#   getRandom() → 1 or 2 (2/3 chance for 1, 1/3 for 2)
#   remove(1) → True
#
# Time Complexity : O(1) average for all operations
# Space Complexity: O(n) for list and hashmap

import random
from collections import defaultdict

class RandomizedCollection:

    def __init__(self):
        self.random = []
        self.rand_map = defaultdict(list)
        self.i = 0

    def insert(self, val: int) -> bool:
        if val not in self.rand_map:
            self.random.append(val)
            self.rand_map[val].append(self.i)
            self.i += 1
            return True
        else:
            self.random.append(val)
            self.rand_map[val].append(self.i)
            self.i += 1
            return False

    def remove(self, val: int) -> bool:
        if val in self.rand_map:
            ind = self.rand_map[val][-1]
            n = len(self.random) - 1
            if ind != n:
                self.random[n], self.random[ind] = self.random[ind], self.random[n]
                self.rand_map[self.random[ind]].remove(n)
                self.rand_map[self.random[ind]].append(ind)

            self.random.pop()
            self.rand_map[val].pop()
            if not self.rand_map[val]:
                del self.rand_map[val]
            self.i -= 1
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.random)
