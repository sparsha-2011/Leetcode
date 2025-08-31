
# Author: Sparsha Srinath
# Date: 2025-08-19
# Problem: Minimum Subset Sum Difference
# Link: https://practice.geeksforgeeks.org/problems/minimum-sum-partition3317/1
# Tags: Dynamic Programming, Subset Sum, Partition
# Time Complexity: O(N * totalSum)
# Space Complexity: O(N * totalSum)

#User function Template for python3
class Solution:
    def minDifference(self, arr):
        n = len(arr)
        m = sum(arr)  # total sum of array

        # dp[i][j] will be True if a subset of first i elements can form sum j
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        
        # Base case: sum 0 is always possible (by taking empty subset)
        for i in range(n + 1):
            dp[i][0] = True

        # Fill DP table
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if arr[i - 1] <= j:
                    # We can either take this element or skip it
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
                else:
                    # Can't take this element if it's bigger than j
                    dp[i][j] = dp[i - 1][j]
        
        # Now, check all sums possible from 0 to m//2
        # The goal is to find two subsets with sums S1 and S2 minimizing |S1 - S2|
        res_array = []
        for i in range(m // 2 + 1):
            if dp[n][i]:
                res_array.append(i)
        
        # Compute the minimum difference
        mn = float('inf')
        for s1 in res_array:
            mn = min(mn, m - 2 * s1)  # since S2 = m - S1
        
        return mn

