# https://leetcode.com/problems/rotate-image/
from typing import List


def rotate(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)

    for r in range(n):
        for c in range(r + 1, n):
            temp = matrix[r][c] # pythonic way: a, b = b, a!!!!
            matrix[r][c] = matrix[c][r]
            matrix[c][r] = temp

    for r in range(n):
        for c in range(n // 2):
            temp = matrix[r][c]
            matrix[r][c] = matrix[r][n - 1 - c]
            matrix[r][n - 1 - c] = temp
