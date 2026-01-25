# Author: Sparsha Srinath
# Date: 2025-08-11
# Problem: Search in Bitonic Array
# Link: https://www.geeksforgeeks.org/find-element-bitonic-array/
# Tags: Binary Search, Bitonic Array, Divide and Conquer
# Time Complexity: O(log n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def searchBitonic(self, nums: List[int], target: int) -> int:
        # Step 1: Find peak index
        peak = self.findPeak(nums)
        
        # Step 2: Search in ascending part
        index = self.binarySearch(nums, target, 0, peak, ascending=True)
        if index != -1:
            return index
        
        # Step 3: Search in descending part
        return self.binarySearch(nums, target, peak + 1, len(nums) - 1, ascending=False)
    
    def findPeak(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if nums[mid] < nums[mid + 1]:
                start = mid + 1
            else:
                end = mid
        return start
    
    def binarySearch(self, nums: List[int], target: int, start: int, end: int, ascending: bool) -> int:
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if ascending:
                if nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                if nums[mid] > target:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1
