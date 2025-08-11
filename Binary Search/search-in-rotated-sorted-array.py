
# Author: Sparsha Srinath
# Date: 2025-08-11
# Problem: Search in Rotated Sorted Array
# Link: https://leetcode.com/problems/search-in-rotated-sorted-array/
# Tags: Binary Search, Array, Divide and Conquer
# Time Complexity: O(log n)
# Space Complexity: O(1)


from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        N = len(nums)
        start = 0
        end = N - 1
        res = 0

        # Find the index of the smallest element (rotation pivot)
        while start <= end:
            if nums[start] <= nums[end]:
                res = start
                break
            mid = (start + end) // 2
            prev = (mid + N - 1) % N
            nxt = (mid + 1) % N

            if nums[mid] < nums[prev] and nums[mid] < nums[nxt]:
                res = mid
                break

            if nums[start] <= nums[mid]:
                start = mid + 1
            else:
                end = mid - 1

        # Helper binary search function
        def binary_search(start, end):
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return -1

        left = binary_search(0, res - 1)
        right = binary_search(res, N - 1)
        
        # Debug print - remove or comment out for production
        print(res, left, right)

        if left == right == -1:
            return -1

        if left == -1:
            return right

        return left
