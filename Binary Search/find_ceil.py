# Author: Sparsha Srinath
# Date: 2025-08-17
# Problem: Ceil of an Element in a Sorted Array
# Link: https://practice.geeksforgeeks.org/problems/ceil-the-floor2802/1
# Tags: Binary Search, Array
# Time Complexity: O(log N)
# Space Complexity: O(1)

#User function Template for python3
class Solution:
    def findCeil(self, arr, x):
        # code here
        N = len(arr)
        start, end = 0, N - 1
        res = -1
        while start <= end:
            mid = (start + end) // 2

            if x == arr[mid]:
                res = mid       # track leftmost equal
                end = mid - 1
            elif x > arr[mid]:
                start = mid + 1
            else:
                end = mid - 1   # shrink to left; start will land on ceil

        idx = res if res != -1 else start
        return idx if idx < N else -1
