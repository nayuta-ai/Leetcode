# time O(n) n:number of loop
# space O(n) n:number of loop
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def loop(root):
            if root is None:
                return 
                
            ans.append(root.val)
            loop(root.right)
            loop(root.left)
        
        ans = []
        loop(root)
        ans.reverse()
        return ans