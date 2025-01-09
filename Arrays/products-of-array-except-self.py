# Problem Title: Products of Array Except Self
# Problem URL: https://leetcode.com/problems/product-of-array-except-self/
# Difficulty: Medium

"""
Problem Statement:

Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in O(n) time without using the division operation?

Example 1:

Input: nums = [1,2,4,6]

Output: [48,24,12,8]

Example 2:

Input: nums = [-1,0,1,2,3]

Output: [0,-6,0,0,0]

Constraints:

2 <= nums.length <= 1000
-20 <= nums[i] <= 20
"""

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = [1]
        postfix_prod= [1]
        res = []
        prod=1
        for i in range(len(nums)-1):
           
            prod = prod*nums[i]

            prefix_prod.append(prod)
        
        prod=1
        for i in range(len(nums)-1,0,-1):

            prod = prod*nums[i]
            postfix_prod.append(prod)

        postfix_prod = postfix_prod[::-1]
        
        print(prefix_prod, postfix_prod)
        for i,j in zip(prefix_prod, postfix_prod):
            res.append(i*j)
        return res
