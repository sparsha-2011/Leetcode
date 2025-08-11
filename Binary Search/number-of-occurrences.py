
# Author: Your Name
# Date: 2025-08-10
# Problem: Frequency of an Element in a Sorted Array
# Link: https://practice.geeksforgeeks.org/problems/number-of-occurrence2259/1
# Tags: Binary Search, Array
# Time Complexity: O(log n) - Two binary searches
# Space Complexity: O(1) - Constant extra space


class Solution:
    def countFreq(self, arr, target):
        N = len(arr)
        
        first, last = -1, -1
        
        # Find first occurrence
        start = 0
        end = N - 1
        while start <= end:
            mid = (start + end) // 2
            if target == arr[mid]:
                first = mid
                end = mid - 1
            elif target > arr[mid]:
                start = mid + 1
            else:
                end = mid - 1
        
        # Find last occurrence
        start = 0
        end = N - 1       
        while start <= end:
            mid = (start + end) // 2
            if target == arr[mid]:
                last = mid
                start = mid + 1
            elif target > arr[mid]:
                start = mid + 1
            else:
                end = mid - 1
            
        return 0 if first == -1 and last == -1 else last - first + 1
