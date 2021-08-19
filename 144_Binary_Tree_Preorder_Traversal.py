# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def loop(root, ans):
            if root is None:
                return ans
            else:
                ans.append(root.val)
            if root.right is None and root.left is None:
                return ans
            elif root.right is None:
                return loop(root.left, ans)
            elif root.left is None:
                return loop(root.right, ans)
                
            else:
                loop(root.left, ans)
                loop(root.right, ans)
                return ans
        return loop(root, ans)