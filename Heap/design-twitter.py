# Author: Sparsha Srinath
# Date: 2025-07-19
# Problem: Design Twitter
# Link: https://leetcode.com/problems/design-twitter/
# Tags: HashMap, Heap, Design, Priority Queue
# Time Complexity: O(U * T log (U * T)) for getNewsFeed where U is number of followees and T is tweets per user (worst case)
# Space Complexity: O(U * T) for storing tweets and follow relationships

from collections import defaultdict
import heapq
from typing import List

class Twitter:
    def __init__(self):
        self.tweetMap = defaultdict(list)  # userId -> list of (timestamp, tweetId)
        self.followMap = defaultdict(set)  # userId -> set of followees
        self.timestamp = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.timestamp, tweetId))
        self.timestamp -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []
        res = []
        self.followMap[userId].add(userId)

        for followee in self.followMap[userId]:
            if followee in self.tweetMap:
                for t in self.tweetMap[followee][-10:]:
                    heapq.heappush(minHeap, t)

        while minHeap and len(res) < 10:
            _, tweetId = heapq.heappop(minHeap)
            res.append(tweetId)

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
