# Author: Sparsha Srinath
# Date: 2025-08-16
# Problem: Partition Equal Subset Sum
# Link: https://practice.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1
# Tags: Dynamic Programming, Subset Sum, 2D DP
# Time Complexity: O(n * sum(arr)/2)
# Space Complexity: O(n * sum(arr)/2)

class Solution:
    def equalPartition(self, arr):
        """
        Determines if the array can be partitioned into two subsets with equal sum.

        Parameters:
            arr (List[int]): The input array

        Returns:
            bool: True if the array can be partitioned into equal subsets, False otherwise
        """
        total_sum = sum(arr)
        
        # If total sum is odd, partition is impossible
        if total_sum % 2 != 0:
            return False

        n = len(arr)
        target = total_sum // 2

        # Initialize DP table
        dp = [[False] * (target + 1) for _ in range(n + 1)]

        # Base case: sum 0 is always possible
        for i in range(n + 1):
            dp[i][0] = True

        # Fill the DP table
        for i in range(1, n + 1):
            for j in range(1, target + 1):
                if arr[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j - arr[i - 1]] or dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n][target]
