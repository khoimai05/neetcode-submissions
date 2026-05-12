# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:  
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) 
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.new = None
        self.res = False
        def dfs_s(node,searchNode):
            if self.res == True:
                return
            if node is None :
                return
            if node.val == searchNode.val:
                self.new = node
                self.res = self.isSameTree(subRoot, self.new)  
            dfs_s(node.left,searchNode)
            dfs_s(node.right,searchNode)
        dfs_s(root, subRoot)
        return self.res
        
