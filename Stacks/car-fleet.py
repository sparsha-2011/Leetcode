# File: car_fleet.py
# Author: Sparsha Srinath
# Leetcode Problem: https://leetcode.com/problems/car-fleet/
# Tags: Stack, Greedy, Sorting
# Time Complexity: O(n log n)
# Space Complexity: O(n)

from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Returns the number of car fleets that will arrive at the destination.

        A car fleet is a group of cars driving at the same speed that arrived
        together without overtaking each other.

        Args:
            target (int): The destination distance.
            position (List[int]): The starting positions of the cars.
            speed (List[int]): The speeds of the cars.

        Returns:
            int: The number of car fleets that will arrive at the destination.
        """
        # Pair each car's position with its speed
        pair = [[p, s] for p, s in zip(position, speed)]

        # Sort the cars by position in descending order (closest to target last)
        stack = []
        for p, s in sorted(pair, reverse=True):
            timeToDest = (target - p) / s

            # If this car catches up to the fleet ahead, it joins the fleet (no push)
            if not stack or timeToDest > stack[-1]:
                stack.append(timeToDest)

        return len(stack)
