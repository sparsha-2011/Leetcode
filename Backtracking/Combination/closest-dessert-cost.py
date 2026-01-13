# Date: 2025-04-15
# Author: Sparsha Srinath
# Leetcode (Closest Dessert Cost): https://leetcode.com/problems/closest-dessert-cost/
# Tags: Backtracking, DFS, Set, Greedy

class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        # Set to store all possible topping combinations
        costs = set()

        # DFS to explore topping combinations (each topping can be used 0, 1, or 2 times)
        def dfs(idx, sum_local):
            costs.add(sum_local)
            for i in range(idx, len(toppingCosts)):
                # Use topping once
                dfs(i + 1, sum_local + toppingCosts[i])
                # Use topping twice
                dfs(i + 1, sum_local + toppingCosts[i] * 2)

        # Start DFS with no toppings
        dfs(0, 0)

        # Initialize differences
        closest_pos_diff = float('inf')  # Closest under target
        closest_neg_diff = float('inf')  # Closest over target

        # Combine each base cost with each topping sum
        for base in baseCosts:
            for topping_sum in costs:
                total = base + topping_sum
                diff = target - total
                if diff == 0:
                    return target  # Exact match found
                if diff > 0:
                    closest_pos_diff = min(closest_pos_diff, diff)
                else:
                    closest_neg_diff = min(closest_neg_diff, abs(diff))

        # Decide best option: closest under or over
        if closest_pos_diff == closest_neg_diff:
            return target - closest_pos_diff
        elif closest_pos_diff < closest_neg_diff:
            return target - closest_pos_diff
        else:
            return target + closest_neg_diff
