# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        node = root
        p_list = []
        while node is not None:
            p_list.append([node.val,node])
            if p.val < node.val:
                node = node.left
            elif p.val > node.val:
                node = node.right
            else:
                break
        q_list = []
        node = root
        while node is not None:
            q_list.append([node.val,node])    
            if q.val < node.val:
                node = node.left
            elif q.val > node.val:
                node = node.right
            else:
                break
   
        print(p_list)
        print('&&&&')
        print(q_list)
        prev = root
        for i in range(min(len(p_list),len(q_list))):
            if p_list[i][0] == q_list[i][0]:
                prev = p_list[i][1]
            else:
                break
        return prev