# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        stack = []
        stack.append([root,-100000000,1000000000])
        while stack:
            # print(stack)
            node,l,r = stack.pop()
            if not (l < node.val < r):
                return False

            if node.left:
                    stack.append([node.left,l,node.val])

            if node.right:
                    stack.append([node.right,node.val,r])
        return True