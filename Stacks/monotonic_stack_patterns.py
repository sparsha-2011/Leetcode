# Author: Sparsha Srinath
# Date: 2025-06-29
# Description: Stack-based solutions to find nearest greater/smaller elements
#              to the left and right in an array.
# Tags: Monotonic Stack, Array, Greedy
# Time Complexity: O(n) for each function
# Space Complexity: O(n) for each function

from typing import List

class MonotonicStackSolutions:

    @staticmethod
    def nearest_greater_to_left(arr: List[int]) -> List[int]:
        """
        For each element, find the nearest greater element to its left.

        Returns:
            A list of nearest greater elements to the left or -1 if none exists.
        """
        stack = []
        res = []

        for num in arr:
            while stack and stack[-1] <= num:
                stack.pop()
            res.append(stack[-1] if stack else -1)
            stack.append(num)

        return res

    @staticmethod
    def nearest_greater_to_right(arr: List[int]) -> List[int]:
        """
        For each element, find the nearest greater element to its right.

        Returns:
            A list of nearest greater elements to the right or -1 if none exists.
        """
        stack = []
        res = [0] * len(arr)

        for i in range(len(arr) - 1, -1, -1):
            while stack and stack[-1] <= arr[i]:
                stack.pop()
            res[i] = stack[-1] if stack else -1
            stack.append(arr[i])

        return res

    @staticmethod
    def nearest_smaller_to_left(arr: List[int]) -> List[int]:
        """
        For each element, find the nearest smaller element to its left.

        Returns:
            A list of nearest smaller elements to the left or -1 if none exists.
        """
        stack = []
        res = []

        for num in arr:
            while stack and stack[-1] >= num:
                stack.pop()
            res.append(stack[-1] if stack else -1)
            stack.append(num)

        return res

    @staticmethod
    def nearest_smaller_to_right(arr: List[int]) -> List[int]:
        """
        For each element, find the nearest smaller element to its right.

        Returns:
            A list of nearest smaller elements to the right or -1 if none exists.
        """
        stack = []
        res = [0] * len(arr)

        for i in range(len(arr) - 1, -1, -1):
            while stack and stack[-1] >= arr[i]:
                stack.pop()
            res[i] = stack[-1] if stack else -1
            stack.append(arr[i])

        return res
