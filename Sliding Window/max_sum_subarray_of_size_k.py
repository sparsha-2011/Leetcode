# Author: Sparsha Srinath
# Date: 2025-06-29
# URL: https://www.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1
# Tags: Sliding Window, Arrays
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Description:
#   Given an array of integers and a number k, find the maximum sum
#   of a subarray of size k using the sliding window technique.

class Solution:
    def maximumSumSubarray(self, arr, k):
        """
        Finds the maximum sum of a subarray of size k.

        Args:
            arr (List[int]): Input list of integers.
            k (int): Size of the subarray.

        Returns:
            int: Maximum sum of any subarray of size k.
        """
        max_sum = 0
        cur_sum = 0
        start = 0

        for end in range(len(arr)):
            cur_sum += arr[end]

            if end - start + 1 == k:
                max_sum = max(max_sum, cur_sum)
                cur_sum -= arr[start]
                start += 1

        return max_sum
