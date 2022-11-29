# https://leetcode.com/problems/flood-fill/
from typing import List


def flood_fill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    to_change = [(sr, sc)]
    s_color = image[sr][sc]

    while to_change:
        r, c = to_change.pop()
        if image[r][c] != s_color:
            continue
        s_color = image[r][c]
        if s_color != color:
            image[r][c] = color
            if r - 1 >= 0:
                to_change.append((r - 1, c))
            if r + 1 < len(image):
                to_change.append((r + 1, c))
            if c - 1 >= 0:
                to_change.append((r, c - 1))
            if c + 1 < len(image[0]):
                to_change.append((r, c + 1))

    return image
