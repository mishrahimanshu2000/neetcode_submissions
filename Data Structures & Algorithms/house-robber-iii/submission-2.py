# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        dp = {}
        def helper(root, last):
            if not root:
                return 0
            if (root,last) in dp:
                return dp[(root,last)]
            
            notTake = helper(root.left, False)
            notTake += helper(root.right, False)
        
            take = 0
            if not last:
                take = root.val
                take += helper(root.left, True)
                take += helper(root.right, True)
            res = max(take, notTake)
            dp[(root,last)] = res
            return res
        
        return helper(root, False)