
# Author: Sparsha Srinath
# Date: 2025-08-10
# Problem: Find the Rotation Count in Rotated Sorted Array
# Link: https://practice.geeksforgeeks.org/problems/rotation4723/1
# Tags: Binary Search, Array
# Time Complexity: O(log n) - Modified binary search
# Space Complexity: O(1) - Constant space


class Solution:
    def findKRotation(self, arr):
        n = len(arr)
        start = 0
        end = n - 1

        while start <= end:
            # If the array segment is already sorted, start is the smallest
            if arr[start] <= arr[end]:
                return start

            mid = (start + end) // 2
            prev = (mid + n - 1) % n
            nxt = (mid + 1) % n

            # Check if mid is the rotation point (smallest element)
            if arr[mid] < arr[prev] and arr[mid] < arr[nxt]:
                return mid

            # Decide which half to search
            if arr[mid] >= arr[start]:  
                # Left half sorted, so pivot must be in right half
                start = mid + 1
            else:
                # Right half sorted, so pivot must be in left half
                end = mid - 1

        return 0  # If no rotation
