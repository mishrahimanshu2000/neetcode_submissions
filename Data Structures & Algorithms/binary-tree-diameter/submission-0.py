# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = [0]

        def helper(root):
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            ans[0] = max(ans[0], left+right)
            return 1 + max(right, left)

        helper(root)
        return ans[0]