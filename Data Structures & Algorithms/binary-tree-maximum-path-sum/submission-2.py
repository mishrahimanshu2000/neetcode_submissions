# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def helper(root, ans):
            if not root:
                return 0
            left = max(0,helper(root.left, ans))
            right = max(0,helper(root.right, ans))
            ans[0] = max(ans[0], root.val+left+right)
            return root.val+max(left, right)
            
        ans = [float('-inf')]
        helper(root,ans)
        return ans[0]