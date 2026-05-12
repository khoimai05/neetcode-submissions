# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.total = True
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(node_1, node_2):
            if node_1 is None and node_2 is None:
                return
            if node_1 is None or node_2 is None:
                self.total = False
                return
            #where no node is none
            if node_1.val != node_2.val:
                self.total = False  
            dfs(node_1.left, node_2.left)
            dfs(node_1.right, node_2.right)
            return
        dfs(p,q)
        return self.total
        