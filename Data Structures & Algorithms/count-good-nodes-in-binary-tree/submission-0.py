# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(root, max_val):
            if not root:
                return 0
            total = 0
            if root.val >= max_val:
                total = 1
            total += helper(root.left, max(root.val,max_val));
            total += helper(root.right, max(root.val,max_val))
            return total
        return helper(root, -102)
