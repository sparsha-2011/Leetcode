# Date: 2025-05-26
# Author: Sparsha Srinath
# Leetcode (Number of Squareful Arrays): https://leetcode.com/problems/number-of-squareful-arrays/
# Tags: Backtracking, DFS, Pruning, Sorting, Permutations, Duplicate Handling

from typing import List

class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        cur = []
        used = [False] * len(nums)
        cnt = 0
        nums.sort()

        def is_squareful(a: int, b: int) -> bool:
            s = a + b
            root = int(s ** 0.5)
            return root * root == s

        def dfs(cur: List[int]) -> None:
            nonlocal cnt
            if len(nums) == len(cur):
                cnt += 1
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                # Skip duplicates if the previous identical element is not used (to avoid counting duplicates)
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                # Check if current number and last number in cur form a squareful pair
                if cur and not is_squareful(cur[-1], nums[i]):
                    continue

                used[i] = True
                cur.append(nums[i])
                dfs(cur)
                used[i] = False
                cur.pop()

        dfs(cur)
        return cnt
