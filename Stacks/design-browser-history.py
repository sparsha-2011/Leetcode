# Author: Sparsha Srinath
# Date: 2025-07-19
# Problem: Design Browser History
# Link: https://leetcode.com/problems/design-browser-history/
# Tags: Stack, Design
# Time Complexity: 
#   - visit: O(1)
#   - back: O(k), where k = steps or size of history stack
#   - forward: O(k), where k = steps or size of forward stack
# Space Complexity: O(n), where n is the total number of visited URLs

class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur_stack = [homepage]       # stack to hold history up to current page
        self.forward_stack = []           # stack to hold forward history

    def visit(self, url: str) -> None:
        self.cur_stack.append(url)
        self.forward_stack.clear()        # clear forward history when new URL is visited

    def back(self, steps: int) -> str:
        while steps and len(self.cur_stack) > 1:
            self.forward_stack.append(self.cur_stack.pop())
            steps -= 1
        return self.cur_stack[-1]

    def forward(self, steps: int) -> str:
        while steps and self.forward_stack:
            self.cur_stack.append(self.forward_stack.pop())
            steps -= 1
        return self.cur_stack[-1]
