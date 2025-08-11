# Author: Sparsha Srinath
# Date: 2025-08-11
# Problem: Search in a Sorted Array of Unknown Size
# Link: https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/
# Tags: Binary Search, Array
# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        left, right = 0, 1
        
        # Expand range exponentially until target is within range
        while reader.get(right) < target:
            left = right
            right <<= 1  # double the index
        
        # Standard binary search within the identified range
        while left <= right:
            mid = left + (right - left) // 2
            val = reader.get(mid)
            
            if val == target:
                return mid
            elif val > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1
