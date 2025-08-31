```python
# Author: Sparsha Srinath
# Date: 2025-08-19
# Problem: Count Partitions With Given Difference
# Link: https://practice.geeksforgeeks.org/problems/partitions-with-given-difference/1
# Tags: Dynamic Programming, Subset Sum, Partition DP
# Time Complexity: O(N * target)
# Space Complexity: O(N * target)

from typing import List

class Solution:
    def countPartitions(self, arr: List[int], d: int) -> int:
        n = len(arr)
        total = sum(arr)  # total sum of array

        # If the difference is greater than total sum OR (total + d) is odd,
        # then it is not possible to partition into subsets with difference d
        if d > total or (total + d) % 2 != 0:
            return 0

        # Target sum for one subset is derived as (total + d) // 2
        target = (total + d) // 2

        # dp[i][j] = number of ways to form sum j using first i elements
        dp = [[0] * (target + 1) for _ in range(n + 1)]

        # Base case: there is 1 way to form sum 0 (take empty subset)
        dp[0][0] = 1

        # Fill DP table
        for i in range(1, n + 1):
            for j in range(target + 1):
                if arr[i - 1] <= j:
                    # Choice 1: exclude current element
                    # Choice 2: include current element
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - arr[i - 1]]
                else:
                    # Current element too large, can't include it
                    dp[i][j] = dp[i - 1][j]

        # Final answer: number of ways to reach target sum
        return dp[n][target]
```
