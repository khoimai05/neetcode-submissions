# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True  # Global variable to track balance status
        
        def height(node):
            if not node or not self.balanced:
                return 0
            
            left_height = height(node.left)
            right_height = height(node.right)
            
            if abs(left_height - right_height) > 1:
                self.balanced = False
            
            return max(left_height, right_height) + 1
        
        height(root)
        return self.balanced
        