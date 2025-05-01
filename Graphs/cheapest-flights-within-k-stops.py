
# Author: Sparsha Srinath
# URL: https://leetcode.com/problems/cheapest-flights-within-k-stops/
# Date: 2025-04-23
# Tags: graph, bellman-ford, dynamic-programming, shortest-path

from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Initialize prices from src to all nodes as infinity, except src itself
        prices = [float('inf')] * n
        prices[src] = 0

        # Perform Bellman-Ford relaxation up to k+1 times (k stops = k+1 edges)
        for _ in range(k + 1):
            tmpPrices = prices.copy()  # Prevent mid-iteration contamination
            for s, d, p in flights:
                if prices[s] == float('inf'):
                    continue
                # Relax edge (s -> d) if a cheaper cost is found
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices

        # Return result, -1 if destination is unreachable within k stops
        return -1 if prices[dst] == float('inf') else prices[dst]
