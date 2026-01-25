# Author: Sparsha Srinath
# Date: 2025-08-19
# Problem: Search a 2D Matrix
# Link: https://leetcode.com/problems/search-a-2d-matrix/
# Tags: Binary Search, Matrix
# Time Complexity: O(log (M*N))
# Space Complexity: O(1)

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        M, N = len(matrix[0]), len(matrix)  # M = cols, N = rows
        start, end = 0, M * N - 1

        while start <= end:
            mid = (start + end) // 2
            r, c = mid // M, mid % M  # map 1D index to 2D (row, col)

            if target == matrix[r][c]:
                return True
            elif target > matrix[r][c]:
                start = mid + 1
            else:
                end = mid - 1

        return False



# Author: Sparsha Srinath
# Date: 2025-08-17
# Problem: Search a 2D Matrix II
# Link: https://leetcode.com/problems/search-a-2d-matrix-ii/
# Tags: Matrix, Two-Pointer, Binary Search (Staircase)
# Time Complexity: O(M + N)
# Space Complexity: O(1)

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        N, M = len(matrix[0]), len(matrix)  # N = cols, M = rows
        i, j = 0, N - 1  # start at top-right

        while 0 <= i < M and 0 <= j < N:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1  # move down to larger values
            else:
                j -= 1  # move left to smaller values
        return False
