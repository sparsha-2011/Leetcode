# Author: Sparsha Srinath
# Date: 2025-08-13
# Problem: Allocate Minimum Number of Pages
# Link: https://www.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1
# Tags: Binary Search, Greedy, Array, Partition
# Time Complexity: O(n log(sum(arr) - max(arr)))
# Space Complexity: O(1)

class Solution:
    def findPages(self, arr, k):
        # If there are fewer books than students, allocation is impossible
        if k > len(arr):
            return -1
        
        start = max(arr)  # Minimum possible max pages
        end = sum(arr)    # Maximum possible max pages
        res = -1
        
        # Helper function to check if we can allocate with max pages = mx
        def check(mx):
            total = 0
            count = 1
            for i in arr:
                total += i
                if total > mx:
                    count += 1
                    total = i
            return count <= k

        # Binary search for the minimum possible maximum pages
        while start <= end:
            mid = (start + end) // 2
            if check(mid):
                res = mid
                end = mid - 1
            else:
                start = mid + 1
        
        return res
