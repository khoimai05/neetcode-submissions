# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        a = root.left
        b = root.right
        root.left = b 
        root.right = a
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root