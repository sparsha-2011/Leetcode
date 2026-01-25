
# Author: Sparsha Srinath
# Date: 2025-08-19
# Problem: Find in Mountain Array
# Link: https://leetcode.com/problems/find-in-mountain-array/
# Tags: Binary Search, Peak Finding, Interactive
# Time Complexity: O(log N) MountainArray.get calls
# Space Complexity: O(1)

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        
        def binary_search(start, end, asc):
            while start <= end:
                mid = (start + end) // 2
                if mountainArr.get(mid) == target:
                    return mid
                if asc:
                    if target > mountainArr.get(mid):
                        start = mid + 1
                    else:
                        end = mid - 1
                else:
                    if target > mountainArr.get(mid):
                        end = mid - 1
                    else:
                        start = mid + 1
            return -1
        
        N = mountainArr.length()
        start, end = 0, N - 1

        # Find peak index
        while start < end:
            mid = (start + end) // 2
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                start = mid + 1
            else:
                end = mid
        peak = start

        if target == mountainArr.get(peak):
            return peak

        # Search in ascending half
        res1 = binary_search(0, peak - 1, True)
        if res1 != -1:
            return res1

        # Search in descending half
        return binary_search(peak, N - 1, False)

