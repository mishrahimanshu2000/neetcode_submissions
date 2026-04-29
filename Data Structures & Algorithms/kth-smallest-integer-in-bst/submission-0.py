# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        rs = [k,None]
        def dfs(root, rs):
            if not root:
                return 
            
            dfs(root.left, rs)
            if rs[0] == 0:
                return 
            rs[0] -= 1
            if rs[0] == 0:
                rs[1] = root.val
                return 
            dfs(root.right, rs)
        
        dfs(root,rs)
        return rs[1]