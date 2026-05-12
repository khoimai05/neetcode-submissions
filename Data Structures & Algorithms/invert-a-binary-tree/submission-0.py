class Solution:
    def flip(self, root: Optional[TreeNode]):
        if root == None:
            return
        temp = root.left
        root.left = root.right
        root.right = temp
        self.flip(root.left)
        self.flip(root.right)

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.flip(root)
        return root
