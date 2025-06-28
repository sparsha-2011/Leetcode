
# Author: Sparsha Srinath
# Leetcode Problem: https://leetcode.com/problems/min-stack/
# Tags: Stack, Design, Data Structures
# Time Complexity: O(1) for all operations
# Space Complexity: O(n)

# ---------------------
# Approach 1: Encoded Minimum Values
# ---------------------

class MinStack:
    """
    Approach 1:
    Uses a mathematical encoding trick to store the minimum without an extra stack.
    Encodes the previous min in the current value when pushing a new minimum.
    """

    def __init__(self):
        self.stack = []
        self.minVal = None

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.minVal = val
        else:
            if val < self.minVal:
                # Encode current value to store previous min
                encoded_val = 2 * val - self.minVal
                self.stack.append(encoded_val)
                self.minVal = val
            else:
                self.stack.append(val)

    def pop(self) -> None:
        if not self.stack:
            return
        val = self.stack.pop()
        if val < self.minVal:
            # Decode previous min value
            self.minVal = 2 * self.minVal - val
        if not self.stack:
            self.minVal = None

    def top(self) -> int:
        if not self.stack:
            return None
        val = self.stack[-1]
        if val < self.minVal:
            return self.minVal
        return val

    def getMin(self) -> int:
        return self.minVal



# ---------------------
# Approach 2: Dual Stack (Main Stack + Min Stack)
# ---------------------

class MinStack:
    """
    Approach 2:
    Uses two stacks: one for all values and another to keep track of the current minimum.
    """

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        current_min = val if not self.minStack else min(val, self.minStack[-1])
        self.minStack.append(current_min)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

