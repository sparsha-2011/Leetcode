# Author: Sparsha Srinath
# Date: 2025-08-19
# Problem: Median of Two Sorted Arrays
# Link: https://leetcode.com/problems/median-of-two-sorted-arrays/
# Tags: Binary Search, Divide and Conquer, Two Arrays
# Time Complexity: O(log(min(M, N)))
# Space Complexity: O(1)

from typing import List
import math

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A
        M, N = len(A), len(B)

        start, end = 0, M
        half = (M + N + 1) // 2

        while start <= end:
            mid = (start + end) // 2
            mid2 = half - mid

            L1 = A[mid - 1] if mid > 0 else -math.inf
            R1 = A[mid] if mid < M else math.inf
            L2 = B[mid2 - 1] if mid2 > 0 else -math.inf
            R2 = B[mid2] if mid2 < N else math.inf

            if L1 > R2:
                end = mid - 1
            elif L2 > R1:
                start = mid + 1
            else:
                if (M + N) % 2 == 1:
                    return float(max(L1, L2))
                return float((max(L1, L2) + min(R1, R2)) / 2.0)
