# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isValid(root, fr, to):
            if not root:
                return True
            
            val = root.val
            if val <= fr or val >= to:
                return False
            return isValid(root.left, fr, val) and isValid(root.right, val, to)
        
        return isValid(root, float('-inf'), float('inf'))