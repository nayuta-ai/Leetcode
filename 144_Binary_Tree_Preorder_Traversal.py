# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# time O(n) n:number of loop
# soace O(n) n:number of loop
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def loop(root):
            if root is None:
                return 
            ans.append(root.val)
            loop(root.left)
            loop(root.right)

        ans = []
        loop(root)
        return ans