# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        self.grand_list = []
        def dfs(root,lev):
            if root == None:
                return
            if len(self.grand_list) < lev:
                # print('apendding at')
                # print(self.grand_list)
                self.grand_list.append([])  # adds one empty sublist
            self.grand_list[lev - 1].append(root.val)
            dfs(root.left, lev + 1)
            dfs(root.right, lev + 1)
        dfs(root,1)
        return self.grand_list
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        lister = self.levelOrder(root)
        res = []
        for i in lister:
            res.append(i[-1])
        return res

        