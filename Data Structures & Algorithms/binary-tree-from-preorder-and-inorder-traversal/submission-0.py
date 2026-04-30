# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        d = {}
        n = len(inorder)
        for i in range(n):
            d[inorder[i]] = i
        self.idx = 0
        def helper(start, end):
            if start > end:
                return None
            val = preorder[self.idx]
            self.idx += 1
            i = d[val]
            node = TreeNode(val)
            node.left = helper(start, i-1)
            node.right = helper(i+1, end)
            return node
        return helper(0,n-1)