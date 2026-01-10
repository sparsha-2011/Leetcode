# Author: Sparsha Srinath
# URL: https://leetcode.com/problems/open-the-lock/
# Date: 2025-04-23
# Tags: bfs, graphs, shortest-path, state-space, open-lock

from collections import deque
from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        
        if "0000" in dead:
            return -1
        
        q = deque(["0000"])
        visited = set(["0000"])
        steps = 0
        
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                
                if curr == target:
                    return steps
                
                # generate neighbors
                for i in range(4):
                    digit = int(curr[i])
                    
                    for move in (-1, 1):
                        new_digit = (digit + move) % 10
                        nxt = curr[:i] + str(new_digit) + curr[i+1:]
                        
                        if nxt not in visited and nxt not in dead:
                            visited.add(nxt)
                            q.append(nxt)
            
            steps += 1
        
        return -1
