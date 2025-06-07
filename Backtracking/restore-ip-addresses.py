# Date: 2025-04-15
# Author: Sparsha Srinath
# Leetcode (Restore IP Addresses): https://leetcode.com/problems/restore-ip-addresses/
# Tags: Backtracking, DFS, String Manipulation

from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        """
        Restore all possible valid IP addresses from a string of digits.

        An IP address must have exactly four integers separated by dots,
        each between 0 and 255, and must not contain leading zeros.

        Args:
            s (str): The input string containing only digits.

        Returns:
            List[str]: All valid IP addresses that can be formed.
        """
        res = []

        def is_valid(seg: str) -> bool:
            """
            Check if the given segment is a valid IP section.

            Args:
                seg (str): Segment of the IP address.

            Returns:
                bool: True if valid, False otherwise.
            """
            if len(seg) == 0 or (len(seg) > 1 and seg[0] == '0'):
                return False
            return 0 <= int(seg) <= 255

        def dfs(cur_str: str, idx: int, quarter: int) -> None:
            """
            Perform DFS to explore all segmentations of the IP address.

            Args:
                cur_str (str): Current IP address string being built.
                idx (int): Current index in the input string.
                quarter (int): Number of segments (quarters) used so far.
            """
            if idx == len(s) and quarter == 4:
                res.append(cur_str[:-1])  # Remove trailing '.'
                return
            if quarter >= 4:
                return

            for i in range(1, 4):  # Try segments of length 1, 2, and 3
                if idx + i > len(s):
                    break
                seg = s[idx:idx+i]
                if is_valid(seg):
                    dfs(cur_str + seg + '.', idx + i, quarter + 1)

        dfs('', 0, 0)
        return res


##Approach 2

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        """
        Given a string containing only digits, return all possible valid IP address combinations 
        that can be formed by inserting three dots into the string.

        Args:
            s (str): The input string containing digits.

        Returns:
            List[str]: A list of valid IP address combinations.
        """

        res = []       # Stores all valid IP combinations
        cur = []       # Temporary list to build segments

        def dfs(idx: int, parts: int) -> None:
            """
            Performs depth-first search to generate all valid IP address combinations.

            Args:
                idx (int): Current index in the input string.
                parts (int): Number of parts (segments) formed so far.
            """
            if idx == len(s) and parts == 4:
                res.append('.'.join(cur))
                return
            if parts >= 4:
                return
            
            # Try segments of length 1 to 3
            for i in range(1, 4):
                if idx + i > len(s):
                    break

                segment = s[idx:idx+i]

                # Skip if segment is not valid (e.g., "00", "256", etc.)
                if (segment[0] == '0' and len(segment) > 1) or int(segment) > 255:
                    continue

                cur.append(segment)
                dfs(idx + i, parts + 1)
                cur.pop()  # Backtrack

        dfs(0, 0)
        return res
