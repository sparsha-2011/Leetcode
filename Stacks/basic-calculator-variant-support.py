# Author: Sparsha Srinath  
# Date: 2025-06-29  
# Problem: Basic Calculator (I, II, III variant support)  
# Link: https://leetcode.com/problems/basic-calculator/  
# Tags: Stack, Math, String, Parsing  
# Time Complexity: O(n), where n = length of the string  
# Space Complexity: O(n) for the stack and context stack

class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "") + "+"
        stack = []
        context_stack = []

        op = "+"
        num = 0

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == "(":
                context_stack.append((stack, op))
                stack = []
                num = 0
                op = "+"
            elif c in "-+*/)":
                if op == "+":
                    stack.append(num)
                elif op == "-":
                    stack.append(-num)
                elif op == "*":
                    stack.append(stack.pop() * num)
                elif op == "/":
                    stack.append(int(stack.pop() / num))
                num = 0
                op = c
                if c == ")":
                    num = sum(stack)
                    stack, op = context_stack.pop()

        return sum(stack)
