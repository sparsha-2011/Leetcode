# Author: Sparsha Srinath
# Date: 2025-08-11
# Problem: First Occurrence of 1 in an Infinite Sorted Binary Array
# Link: N/A (Pattern: Exponential Search + Binary Search)
# Tags: Binary Search, Array
# Time Complexity: O(log n)
# Space Complexity: O(1)

def first_one_in_infinite_binary_array(reader):
    left, right = 0, 1

    # Expand the search range until we find a 1
    while reader.get(right) == 0:
        left = right
        right <<= 1  # double the range

    # Binary search within the found range to locate first 1
    ans = -1
    while left <= right:
        mid = left + (right - left) // 2
        if reader.get(mid) == 1:
            ans = mid
            right = mid - 1  # search left for earlier occurrence
        else:
            left = mid + 1
    return ans
