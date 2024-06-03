# https://leetcode.com/problems/reduce-array-size-to-the-half/description/
from collections import Counter
from typing import List


def min_set_size(self, arr: List[int]) -> int:
    removed_len = 0
    num_removed = 0
    # O(n) for constructing Counter / O(nlogn) for sorting (most_common)
    for _, v in Counter(arr).most_common():
        num_removed += 1
        removed_len += v
        if removed_len >= len(arr) / 2:
            break
    return num_removed
