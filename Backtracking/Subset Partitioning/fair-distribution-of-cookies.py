# Author: Sparsha Srinath
# Date: 2025-08-13
# Problem: Fair Distribution of Cookies
# Link: https://leetcode.com/problems/fair-distribution-of-cookies/
# Tags: Backtracking, Recursion, Pruning
# Time Complexity: O(k^n) in the worst case (with pruning in practice)
# Space Complexity: O(k) for buckets + recursion stack

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        cookies.sort(reverse=True)
        buckets = [0]*k
        res = float('inf')
        def backtrack(i):
            nonlocal res
            if i==len(cookies):
                res = min(res,max(buckets))
                return 

            for b in range(k):
                
                
                buckets[b]+=cookies[i]
                if max(buckets)<res:
                    backtrack(i+1)
                buckets[b]-=cookies[i]

                if buckets[b]==0:
                    break
        
        
        
        backtrack(0)
        return res
