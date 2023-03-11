# https://leetcode.com/problems/range-sum-of-bst/description/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def range_sum_bst(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # using nested function
        def sum_nodes(node):
            current_node = node
            current_sum = 0
            if current_node:
                if low <= current_node.val <= high:
                    current_sum += current_node.val
                if current_node.val > low:
                    current_sum += sum_nodes(current_node.left)
                if current_node.val < high:
                    current_sum += sum_nodes(current_node.right)

            return current_sum

        return sum_nodes(root)
