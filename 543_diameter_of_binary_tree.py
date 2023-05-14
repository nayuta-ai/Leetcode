from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_sum = 0
        return max(self.dfs(root.left) + self.dfs(root.right), self.max_sum)

    def dfs(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.dfs(root.left)
        right = self.dfs(root.right)
        self.max_sum = max(self.max_sum, left+right)
        return max(left, right) + 1