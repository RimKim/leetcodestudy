# https://leetcode.com/problems/invert-binary-tree/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invert_tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        # DFS - Pre-Order traversal
        # Post-Order also works - is it faster than Pre-Order?
        # In-Order does not work because the root nodes swaps sides again
        # after the left descendant were swapped
        temp = root.left
        root.left = root.right
        root.right = temp
        self.invert_tree(root.left)
        self.invert_tree(root.right)

        return root
