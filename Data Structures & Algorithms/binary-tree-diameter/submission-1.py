# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.total = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        leftH = self.maxDepth(root.left) + 1
        rightH = self.maxDepth(root.right) + 1
        return max(leftH, rightH)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        self.total = max(self.total, l + r)

        self.diameterOfBinaryTree(root.left)
        self.diameterOfBinaryTree(root.right)

        return self.total
