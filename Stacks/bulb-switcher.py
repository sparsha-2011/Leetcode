# Author: Sparsha Srinath
# Leetcode Problem: https://leetcode.com/problems/bulb-switcher/
# Tags: Math, Insight
# Time Complexity: O(1)
# Space Complexity: O(1)

class Solution:
    def bulbSwitch(self, n: int) -> int:
        """
        Returns the number of bulbs that remain on after n rounds.

        A bulb toggles in each round where its position is divisible by the round number.
        Only bulbs at positions that are perfect squares have an odd number of divisors,
        and thus remain on after all rounds.

        Args:
            n (int): The total number of bulbs and rounds.

        Returns:
            int: The number of bulbs that are on at the end.
        """
        return int(n**0.5)
