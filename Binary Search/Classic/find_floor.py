# Author: Sparsha Srinath
# Date: 2025-08-17
# Problem: Floor of an Element in a Sorted Array
# Link: https://www.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/1
# Tags: Binary Search, Array
# Time Complexity: O(log N)
# Space Complexity: O(1)

#User function Template for python3
class Solution:
    def findFloor(self, arr, x):
        # code here
        N = len(arr)
        start, end = 0, N - 1
        res = -1

        while start <= end:
            mid = (start + end) // 2
            if x == arr[mid]:
                res = mid        # track rightmost equal
                start = mid + 1  # move right to find last occurrence
            elif x > arr[mid]:
                start = mid + 1  # floor is to the right
            else:
                end = mid - 1    # shrink to the left

        idx = res if res != -1 else end  # if no equal, end points to largest < x
        return idx if idx >= 0 else -1
