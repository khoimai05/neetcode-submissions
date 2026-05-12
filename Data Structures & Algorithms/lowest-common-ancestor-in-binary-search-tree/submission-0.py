class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left  # Both nodes are on the left
            elif p.val > root.val and q.val > root.val:
                root = root.right  # Both nodes are on the right
            else:
                return root  # Split happens here; this is the LCA
