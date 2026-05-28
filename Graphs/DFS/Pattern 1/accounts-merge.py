# Author: Sparsha Srinath
# URL: https://leetcode.com/problems/accounts-merge/
# Date: 2026-05-25
# Tags: graph, dfs, hash-map, connected-components, sorting
# Description:
#   Given accounts where each has a name and emails, merge accounts that share
#   any email (they belong to the same person). Preprocessing: map each email to
#   which account indices contain it. If an email appears in multiple accounts,
#   connect those accounts via adjacency list (first account as hub to avoid O(n²)
#   edges). Then use DFS Pattern 1 to find connected components. Each component
#   is one person — collect all their emails, deduplicate, sort, and prepend name.
#
# Preprocessing Steps:
#   1. email_to_accounts: email → list of account indices that contain it
#   2. adjacency list: connect accounts sharing an email (hub pattern)
#   3. DFS to find components of connected accounts
#   4. Collect and sort emails per component
#
# Input: accounts (List[List[str]])
# Output: List[List[str]] — merged accounts with sorted emails
#
# Example:
#   Input : [["John","john@mail.com","john_work@mail.com"],
#            ["John","john@mail.com","john_home@mail.com"],
#            ["Mary","mary@mail.com"]]
#   Output: [["John","john@mail.com","john_home@mail.com","john_work@mail.com"],
#            ["Mary","mary@mail.com"]]
#
# Time Complexity : O(n * k * log(n * k)) where n = accounts, k = max emails per account
# Space Complexity: O(n * k) for maps and adjacency list

from collections import defaultdict
from typing import List

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_accounts = defaultdict(list)
        for i, account in enumerate(accounts):
            for email in account[1:]:
                email_to_accounts[email].append(i)

        adjL = defaultdict(list)
        components = []
        for email, users in email_to_accounts.items():
            for u in range(1, len(users)):
                adjL[users[0]].append(users[u])
                adjL[users[u]].append(users[0])

        visit = set()
        n = len(accounts)

        def dfs(node, comp):
            visit.add(node)
            comp.append(node)
            for nei in adjL[node]:
                if nei not in visit:
                    dfs(nei, comp)

        for i in range(n):
            if i not in visit:
                component = []
                dfs(i, component)
                components.append(component)

        result = []
        for component in components:
            name = accounts[component[0]][0]
            emails = set()
            for idx in component:
                for email in accounts[idx][1:]:
                    emails.add(email)
            result.append([name] + sorted(list(emails)))

        return result
