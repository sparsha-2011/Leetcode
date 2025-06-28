
# Author: Sparsha Srinath
# Leetcode Problem: https://leetcode.com/problems/asteroid-collision/
# Tags: Stack, Simulation
# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        Simulates the collision of asteroids moving along a 1D plane.

        Positive values represent asteroids moving right,
        negative values represent asteroids moving left.

        Collisions occur when a right-moving asteroid meets a left-moving asteroid.
        The smaller one (by absolute value) explodes, or both if equal.

        Args:
            asteroids (List[int]): List of integers representing asteroids.

        Returns:
            List[int]: The state of asteroids after all collisions.
        """
        stack = []

        for asteroid in asteroids:
            while stack and stack[-1] > 0 and asteroid < 0:
                top = stack[-1]
                if abs(top) < abs(asteroid):
                    stack.pop()  # Top asteroid explodes
                elif abs(top) == abs(asteroid):
                    stack.pop()  # Both explode
                    break
                else:
                    break  # Current asteroid explodes
            else:
                # No collision or current asteroid survived all collisions
                stack.append(asteroid)

        return stack
