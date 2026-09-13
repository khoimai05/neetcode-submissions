# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        dicter = defaultdict(list)
        q = deque()
        q.append([root,1])
        dicter[1].append(root.val)
        while q:
            node,val = q.popleft()
            if node.left:
                q.append([node.left,val+1])
                dicter[val+1].append(node.left.val)
            if node.right:
                q.append([node.right,val+1])
                dicter[val+1].append(node.right.val)
        # print(dicter.values())
        return list(i for i in dicter.values())
